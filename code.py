import random
import math
import html

def lambda_handler(event, context):

    particles = []

    random.seed()

    for _ in range(180):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        size = random.uniform(1, 4)
        speed = random.uniform(0.2, 1.2)

        particles.append(
            f'<circle cx="{x}vw" cy="{y}vh" r="{size}" '
            f'class="p" style="--speed:{speed}s"/>'
        )

    particle_data = "\n".join(particles)

    page = f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
      initial-scale=1.0">

<title>AWS Lambda</title>

<style>

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

html, body {{
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #02020a;
    font-family: Arial, sans-serif;
}}

canvas {{
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
}}

.overlay {{
    position: fixed;
    inset: 0;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    pointer-events: none;
}}

.title {{
    font-size: clamp(40px, 8vw, 110px);
    font-weight: 800;
    letter-spacing: 12px;

    color: white;

    text-shadow:
        0 0 10px #00ffff,
        0 0 30px #00ffff,
        0 0 60px #0066ff;

    animation: pulse 3s infinite alternate;
}}

.subtitle {{
    margin-top: 20px;

    font-size: clamp(12px, 2vw, 20px);
    letter-spacing: 7px;

    color: #00ffff;

    opacity: 0.8;
}}

.status {{
    position: absolute;
    bottom: 30px;

    font-family: monospace;
    font-size: 13px;

    color: #6666aa;
}}

@keyframes pulse {{
    from {{
        transform: scale(1);
        opacity: 0.8;
    }}

    to {{
        transform: scale(1.03);
        opacity: 1;
    }}
}}

</style>

</head>

<body>

<canvas id="canvas"></canvas>

<div class="overlay">

    <div class="title">
        LAMBDA
    </div>

    <div class="subtitle">
        PYTHON • SERVERLESS • ONLINE
    </div>

    <div class="status">
        ● AWS FUNCTION ACTIVE
    </div>

</div>

<script>

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let particles = [];

function resize() {{
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}}

window.addEventListener("resize", resize);
resize();

for (let i = 0; i < 180; i++) {{

    particles.push({{

        x: Math.random() * canvas.width,

        y: Math.random() * canvas.height,

        vx: (Math.random() - 0.5) * 0.5,

        vy: (Math.random() - 0.5) * 0.5,

        size: Math.random() * 3 + 1

    }});

}}

function animate() {{

    ctx.fillStyle = "rgba(2, 2, 10, 0.15)";

    ctx.fillRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    const cx = canvas.width / 2;
    const cy = canvas.height / 2;

    particles.forEach((p, i) => {{

        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0 || p.x > canvas.width)
            p.vx *= -1;

        if (p.y < 0 || p.y > canvas.height)
            p.vy *= -1;

        const dx = p.x - cx;
        const dy = p.y - cy;

        const distance =
            Math.sqrt(dx * dx + dy * dy);

        const alpha =
            Math.max(
                0,
                1 - distance / 700
            );

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI * 2
        );

        ctx.fillStyle =
            `rgba(0, 220, 255, ${{alpha}})`;

        ctx.shadowBlur = 15;
        ctx.shadowColor = "#00ffff";

        ctx.fill();

        ctx.shadowBlur = 0;

    }});

    requestAnimationFrame(animate);

}}

animate();

</script>

</body>
</html>
"""

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html; charset=utf-8"
        },
        "body": page
    }

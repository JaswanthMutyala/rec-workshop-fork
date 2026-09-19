export const handler = async () => {
  const html = `
    <!DOCTYPE html>
    <html>
      <head>
        <title>AWS Student Community Day</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
          body {
            margin: 0;
            min-height: 100vh;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #232f3e, #0b1620);
            color: #f2f2f2;
            display: flex;
            align-items: center;
            justify-content: center;
          }
          .card {
            text-align: center;
            padding: 50px 40px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid #ff9900;
            border-radius: 12px;
            max-width: 600px;
          }
          h1 {
            color: #ff9900;
            font-size: 2.2rem;
            margin-bottom: 10px;
          }
          p {
            color: #cbd5db;
            font-size: 1.1rem;
            margin: 0;
          }
          .badge {
            display: inline-block;
            margin-top: 24px;
            padding: 6px 16px;
            background: #ff9900;
            color: #232f3e;
            font-weight: bold;
            border-radius: 20px;
            font-size: 0.9rem;
          }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>Welcome to AWS Student Community Day</h1>
          <p>Organised by Raghu Engineering College</p>
          <span class="badge">Powered by AWS Lambda</span>
        </div>
      </body>
    </html>
  `;

  return {
    statusCode: 200,
    headers: { "Content-Type": "text/html" },
    body: html,
  };
};

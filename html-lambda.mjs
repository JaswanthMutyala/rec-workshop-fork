export const handler = async () => {
  const html = `
    <!DOCTYPE html>
    <html>
      <head><title>Hello from Lambda</title></head>
      <body style="font-family: sans-serif; padding: 40px;">
        <h1>This page is served straight from Lambda</h1>
        <p>No S3, no API Gateway — just a function returning HTML.</p>
      </body>
    </html>
  `;

  return {
    statusCode: 200,
    headers: { "Content-Type": "text/html" },
    body: html,
  };
};

const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;

const server = http.createServer((req, res) => {
    // 1. Point directly to your single HTML file's location
    const filePath = path.join(__dirname, 'public', 'index.html');

    // 2. Read the file from your drive asynchronously
    fs.readFile(filePath, (err, content) => {
        if (err) {
            // Handle error if you forgot to create the index.html file
            res.writeHead(500, { 'Content-Type': 'text/plain' });
            res.end('Error: Could not find or read index.html');
        } else {
            // Send the file over the network pipeline
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(content);
        }
    });
});

// Start listening on port 3000
server.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
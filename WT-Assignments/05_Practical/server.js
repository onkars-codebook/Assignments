const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = 3000;

const server = http.createServer((req, res) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");

    if (req.method === "OPTIONS") {
        res.writeHead(204);
        res.end();
        return;
    }

    if (req.method === "GET" && req.url === "/") {
        const filePath = path.join(__dirname, "index.html");

        fs.readFile(filePath, "utf-8", (err, content) => {
            if (err) {
                res.writeHead(500, { "Content-Type": "text/plain" });
                res.end("Error loading index.html");
            } else {
                res.writeHead(200, { "Content-Type": "text/html" });
                res.end(content);
            }
        });
    } else if (req.method === "POST" && req.url === "/submit") {
        let body = "";
        req.on("data", chunk => {
            body += chunk.toString();
        });

        req.on("end", () => {
            console.log("Raw Body:", body); // debug

            try {
                const data = JSON.parse(body);

                if (!data.name || !data.email || !data.message) {
                    throw new Error("Missing fields");
                }

                console.log("New Inquiry Received:", data);

                res.writeHead(200, { "Content-Type": "application/json" });
                res.end(JSON.stringify({ status: "success", message: "Thank you! We will get back to you soon." }));
            } catch (error) {
                console.error("Error parsing or processing data:", error);
                res.writeHead(400, { "Content-Type": "application/json" });
                res.end(JSON.stringify({ status: "error", message: "Invalid data received." }));
            }
        });
    } else {
        res.writeHead(404, { "Content-Type": "text/plain" });
        res.end("404 - Page Not Found");
    }
});

server.listen(PORT, () => {
    console.log(`🚀 Server running at http://localhost:${PORT}`);
});

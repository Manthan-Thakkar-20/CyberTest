var http = require("http")
var url = require("url")

console.log("Web server started")

// Change request hostnames
http.createServer((req, res) => {
    if (req.url.startsWith("/login")) {
        console.log("Login requested")
        
        var q = url.parse(req.url, true).query;
        email = q.email
        password = q.password

        var req = http.request({
            hostname: "localhost",
            port: 8000,
            path: `/login?email=${email}&password=${password}`,
            method: "POST",
        }, (resp) => {
            resp.on('data', (chunk) => {
                res.end(chunk)
                console.log("Login request responded to")
            })
        })
        req.on("error", (e) => {
            console.error(`Problem with request: ${e.message}`);
        })
        req.end()
    } else if (req.url.startsWith("/signup")) {
        console.log("Signup requested")

        var q = url.parse(req.url, true).query;
        email = q.email
        password = q.password

        var req = http.request({
            hostname: "localhost",
            port: 8000,
            path: `/signup?email=${email}&password=${password}`,
            method: "POST",
        }, (resp) => {
            resp.on('data', (chunk) => {
                res.end(chunk)
                console.log("Signup request responded to")
            })
        })
        req.on("error", (e) => {
            console.error(`Problem with request: ${e.message}`);
        })
        req.end()      
    } else if (req.url.startsWith("/prep_quiz")) {
        console.log("Quiz requested")

        var q = url.parse(req.url, true).query;
        topic = q.topic
        difficulty = q.difficulty

        var req = http.request({
            hostname: "localhost",
            port: 8000,
            path: `/prep_quiz?topic=${topic}&difficulty=${difficulty}`,
            method: "POST",
        }, (resp) => {
            resp.on('data', (chunk) => {
                res.end(chunk)
                console.log("Quiz request responded to")
            })
        })
        req.on("error", (e) => {
            console.error(`Problem with request: ${e.message}`);
        })
        req.end()
    } else if (req.url.startsWith("/submit_answers")) {
        console.log("Answer submission requested")

        var q = url.parse(req.url, true).query;
        topic = q.topic
        answers = q.answers

        var req = http.request({
            hostname: "localhost",
            port: 8000,
            path: `/submit_answers?topic=${topic}`,
            method: "POST",
        }, (resp) => {
            resp.on('data', (chunk) => {
                res.end(chunk)
                console.log("Answer submission request responded to")
            })
        })
        req.on("error", (e) => {
            console.error(`Problem with request: ${e.message}`);
        })
        req.end(JSON.stringify(answers))        
    }
}).listen(80)

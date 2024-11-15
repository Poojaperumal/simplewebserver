from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html lang="en">
<head>
    <title>configuration of my laptop</title>
</head>
<body >
    <h1 align ="center">configuration of my laptop(Pooja P),24900963)</h1>
    <pre>
        <ul >
        <li><b>Device name</b>       DESKTOP-P1C9LOP</li>
        <li><b>processor </b >       13th Gen Intel(R) Core(TH) i3-1335U 1.30 Ghz</li>
        <li><b>Installed RAM </b>    4.00 GB</li>
        <li><b>Device ID</b>         15EEA3B2-7EF5-4DEC-903D-577382C382C3008</li>
        <li><b>product ID </b>       00342-42709-0080-7-AA861</li>
        <li><b>System type</b>       64-bit operating system, x64-based processor</li>
        <li><b>Pen and Touch</b>     No pen or touch input is available for this display</li>
    </ul>
    </pre>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
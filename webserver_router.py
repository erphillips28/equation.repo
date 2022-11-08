# Python 3 server example

# import necessary classes from http.server module
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    # defines all of the routes for your webserver

    def do_GET(self):

        # http://localhost:8080/
        if self.path == "/":  # home page, like "www.google.com/"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("./index.html") as fn:
                self.wfile.write(bytes(fn.read(), "utf8"))

        # http://localhost:8080/run?TempK=<something>&E_s=<something>&z=<something>&Q=<something>
        # will handle receiving in put from your page
        if self.path.startswith("/run"):
            # parse arguments from GET request
            args = urlparse(self.path)
            print(args)
            self.send_response(200)


if __name__ == "__main__":
    # create the server object
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()  # listen for and serve clients
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

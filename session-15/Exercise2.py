import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8006


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        if self.path == '/':   # MAIN PAGE
            f = open("form2.html", 'r')
            contents = f.read()
            f.close()
        elif '/echo' in self.path:
            if 'chk=on' in self.path:  # IF IT HAS BEEN CHECKED THIS COMMAND WILL BE IN THE GET COMMAND
                message = self.path.split('=')[1]  # I INDEX THE MESSAGE
                message2 = message.split('&')[0]   # I CHOOSE THE FIRST INDEX WHICH IS THE MESSAGE
                message2 = message2.upper() # I CAPITALIZE THE MESSAGE
                contents = """<html><body style="background-color: pink;"><h4>RECIEVED:</h4>"""+ message2 + """<br><a href="/">[Main Page]</a><html><body>"""
            else:
                message = self.path.split('=')[1]
                contents = """<html><body style="background-color: pink;"><h4>RECIEVED:</h4>""" + message + """<br><a href="/">[Main Page]</a><html><body>"""
        else:
            f = open('error.html','r')
            contents = f.read()
            f.close()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
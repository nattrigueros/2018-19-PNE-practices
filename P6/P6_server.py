from Seq import Seq
import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8009


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def validating_sequence(self, s):  # SEE IF THE INTRODUCED SEQUENCE IS VALID
        valid = 'ACTG'
        for letter in s:
            if letter not in valid:
                return False
        return True

    def instructions(self, s1, tool):   # APPLY THE DIFFERENT TOOLS TO THE INTRODUCED SEQUENCE, FROM PRACTICE 3
        if (tool == "len"):
            return s1.length()
        elif (tool == "complement"):
            return s1.complement().get_strbase()
        elif (tool == "reverse"):
            return s1.reverse().get_strbase()
        elif (tool == "countA"):
            return s1.count('A')
        elif (tool == "countT"):
            return s1.count('T')
        elif (tool == "countG"):
            return s1.count("G")
        elif (tool == "countC"):
            return s1.count("C")
        elif (tool == "percA"):
            return s1.perc("A")
        elif (tool == "percT"):
            return s1.perc("T")
        elif (tool == "percG"):
            return s1.perc("G")
        elif (tool == "percC"):
            return s1.perc("C")
        else:
            return "ERROR"

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        if self.path == '/':     # MAIN PAGE
            f = open("P6_form.html", 'r')
            contents = f.read()
            f.close()
        elif '/seq' in self.path:         # SEPARATE THE MESSAGE AND CREATE THE WEBSITE THAT IS GOING TO APPEAR WHEN WRITTEN THE MESSAGE
            contents = """<!DOCTYPE html>
            <html lang ="en">
            <head>
                <meta charset="UTF-8">
                <title>SERVER RESPONSE</title>
            </head>
            <body style="background-color: pink">"""


            request = self.path.split('=')[1]  # CHOOSE THE PART BETWEEN BOTH = SIGNS
            separate = request.split('&')     # CHOOSE THE SEQUENCE PART AND TRANSFORM IT INTO UPPER CASE LETTERS ALWAYS
            DNA_seq = separate[0].upper()
            contents = contents + "<p>DNA Sequence: " + DNA_seq + "</p>"

            if self.validating_sequence(DNA_seq):
                s1 = Seq(DNA_seq)     # CREATE THE SEQ OBJECT
                if 'len=on' in self.path:     # IF THE LENGHT OPTION IS CHOSEN
                    length = s1.length()      # APPLY THE LENGTH TOOL
                    contents = contents + "<p>LENGTH: " + str(length) + "</p>"
                operation = self.path.split('operation=')[1].split("&")[0]  # SEARCH FOR THE TOOL WANTED TO BE APPLIED
                contents = contents + "<p>OPERATION: " + operation + "</p>"
                base = self.path.split('base=')[1].split("&")[0]   # SEARCH FOR THE BASE WANTED TO SEARCH
                contents = contents + "<p>BASE: " + base + "</p>"
                tool = operation + base  # CONCATENATE IN ORDER TO APPLY THE METHOD FROM PRACTICE 3
                response = self.instructions(s1, tool)
                contents = contents + "<p>RESPONSE: " + str(response) + "</p>"

            else:
                contents = contents + "<p>NOT VALID</p>"   # IN THE CASE THE SEQUENCE IS NOT VALID


            contents = contents + """<br> <a href="/"> [Main Page] <a>
                        </body></html>"""                               # RETURN TO MAIN PAGE
        else:
            f = open('error.html','r')
            contents = f.read()        # RAISE AN ERROR
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
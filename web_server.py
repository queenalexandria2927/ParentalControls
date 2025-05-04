import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Define the web server handler and set the document root
class MyRequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Customize the root directory for the webserver to only serve files from the 'webserver' folder
        root_dir = os.path.join(os.getcwd(), 'webserver')
        # Continue to serve the requested path if it's inside the 'webserver' directory
        if not os.path.exists(os.path.join(root_dir, path.lstrip('/'))):
            return os.path.join(root_dir, 'index.html')  # Default to the index.html if the file is not found
        return os.path.join(root_dir, path.lstrip('/'))

def run_web_server():
    # Set the port to 8080 for the web server
    port = 8080
    server_address = ('', port)

    # Create the web server
    httpd = TCPServer(server_address, MyRequestHandler)
    
    # Print the message to indicate that the server is running
    print(f"Starting web server on http://localhost:{port}")
    print("Waiting for requests...")

    # Run the server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nWeb server stopped.")
        httpd.server_close()

if __name__ == "__main__":
    run_web_server()

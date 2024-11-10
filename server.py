from socket import *
import os


HTML_FILES = {
    "/": "index.html",
    "/index.html": "index.html",
    "/about.html": "about.html"
}

def get_html_content(fN):
    """ Helper"""
    try:
        with open(fN, 'r') as file:
            return file.read()
    except IOError:
        return None

def handle_request(request):
    """ Handle http """
    headers = request.split('\n')
    fL = headers[0]
    method, path, _ = fL.split()

   
    if method != 'GET':
        response = "HTTP/1.0 405 Method Not Allowed\n\n"
        return response

  
    fN = HTML_FILES.get(path, None)
    if fN and os.path.exists(fN):
        content = get_html_content(fN)
        response = f"HTTP/1.0 200 OK\n\n{content}"
    else:
        response = "HTTP/1.0 404 NOT FOUND\n\n"
        content = get_html_content("not_found.html")
        if content:
            response += content
    
    return response

def run_server():
    host = "127.0.0.1"
    port = 8080

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, port))

    s.listen(1)

    print("Server Listening for connections on port", port)

    while True:
        cs, client_addr = s.accept()
        print(f"Connection from {client_addr}")

        data = cs.recv(1024)
        request = data.decode()
        print(f"Received request:\n{request}")

        response = handle_request(request)
        cs.sendall(response.encode())
        cs.close()

if __name__ == "__main__":
    run_server()

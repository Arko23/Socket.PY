from socket import *

def send_request(host, port, request):
    cs = socket(AF_INET, SOCK_STREAM)
    cs.connect((host, port))
    cs.sendall(request.encode())

    res = cs.recv(4096).decode()
    print(res)

    cs.close()

if __name__ == "__main__":
    sH = "127.0.0.1"
    sP = 8080

    reqs = [
        "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n",
        "GET /index.html HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n",
        "GET /about.html HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n",
        "GET /invalid HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
    ]

    for req in reqs:
        print(f"Sending request:\n{req}")
        send_request(sH, sP, req)
        print("\n" + "-"*50 + "\n")

import socket

s = socket.socket()
s.bind(("127.0.0.1",3000))
s.listen(5)

while True:
    connection, address = s.accept()
    request_data = connection.recv(1024)
    print("Request:")
    print(request_data.decode('utf-8'))
    print("__________________________")
    print(address)
    response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    connection.sendall(response)
    connection.close()

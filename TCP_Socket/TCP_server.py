import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(5)
print("Server is listening...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received from client: {message}")

        # Echo the received message back to the client
        client_socket.send(data)

    client_socket.close()

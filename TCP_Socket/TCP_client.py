import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

try:
    while True:
        message = input("Enter a message to send to the server (or type 'exit' to quit): ")
        client_socket.send(message.encode())

        if message.lower() == "exit":
            break

        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

except KeyboardInterrupt:
    pass

client_socket.close()

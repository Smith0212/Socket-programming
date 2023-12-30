
import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5500

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
 
    print(f"UDP Server listening on {host}: {port}") 

    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode()
        # print(data)

        if data == "EXIT":
            print("Client disconnected.")
            break

        print(f"Client: {data}")

        data = data.upper()
        data = data.encode()
        server.sendto(data, addr)
        
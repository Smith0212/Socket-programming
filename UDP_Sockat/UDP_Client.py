import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5500
    addr = (host, port)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = input("Enter a word: ")

        if data == "EXIT":
            data = data.encode()
            client.sendto(data, addr)

            print("Disconneted from the server.")
            break

        data = data.encode()
        client.sendto(data, addr)

        data, addr = client.recvfrom(1024)
        data = data.decode()
        print(f"Server: {data}")
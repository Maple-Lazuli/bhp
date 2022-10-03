import socket

if __name__ == "__main__":
    target = "127.0.0.1"

    target_port = 9997

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # No connection since UDP
    client.sendto(b"AAABBBCCC", (target, target_port))

    data, addr = client.recvfrom(4096)

    print(data.decode())

    client.close()

import socket

from utils import import_config, mod2div


def decode_data(data, key):
    l_key = len(key)

    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)

    return remainder


def main():
    host, port, key = import_config()
    server = (host, port)

    s = socket.socket()
    print("[INFO] Socket created")

    s.bind(server)
    print(f"[INFO] Socket bound to {port}")

    s.listen(5)

    print("[INFO] Socket is listening")

    while True:
        c, addr = s.accept()
        print(f"[INFO] Got connection from {addr}")

        data = c.recv(1024).decode()

        print(f"[INFO] Received data: {data}")

        if not data:
            break

        ans = decode_data(data, key)
        print(f"[INFO] Remainder after decoding is: {ans}")

        temp = "0" * (len(key) - 1)

        if ans == temp:
            message = "[INFO] No error in data"

        else:
            message = "[ERROR] Error in data"

        c.sendall(message.encode())
        c.close()


if __name__ == "__main__":
    main()

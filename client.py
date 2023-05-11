import socket

from utils import import_config, mod2div


def encode_data(data, key):
    l_key = len(key)

    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)

    codeword = data + remainder
    return codeword


def main():
    host, port, key = import_config()
    server = (host, port)

    s = socket.socket()
    s.connect(server)

    input_string = input("Enter data you want to send: ")
    data = (''.join(format(ord(x), 'b') for x in input_string))
    print("Entered data in binary format: ", data)

    ans = encode_data(data, key)
    print("Encoded data to be sent to server in binary format: ", ans)
    s.sendto(ans.encode(), server)

    print("Received feedback from server: ", s.recv(1024).decode())

    s.close()


if __name__ == "__main__":
    main()

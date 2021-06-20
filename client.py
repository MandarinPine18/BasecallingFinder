import socket

HOST = 'localhost'  # will send to localhost (127.0.0.1)
PORT = 9999         # will send to port 9999

data = []

while True:
    try:
        inputData = input('Input data (comma-separated): ')         # getting raw input
        data = [float(i.strip()) for i in inputData.split(',')]     # processing to float list for uniformity, client-side input checking
        break
    except ValueError:
        print("Requires comma-separated floats, please retry\n")


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(repr(data), 'utf-8'))        # encoding, sending float list
        print(sock.recv(2048).decode('utf-8'))          # receiving, decoding, outputting list of basecallings
except ConnectionRefusedError:
    print("Connection not established, please try again later")
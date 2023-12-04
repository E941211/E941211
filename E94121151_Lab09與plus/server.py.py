import socket

HOST = '192.168.137.73'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    outdata = input("Enter a number (or 'exit' to close): ")
    if outdata.lower() == 'exit':
        break

    print('Send: ' + outdata)
    s.sendall(outdata.encode('utf-8'))

    indata = s.recv(1024).decode('utf-8')
    print('Received: ' + indata)

s.close()

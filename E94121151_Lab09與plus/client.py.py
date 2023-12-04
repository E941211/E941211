import socket

HOST = '192.168.137.73'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    outdata = input("Enter a number (or 'exit' to close): ")
    if outdata.lower() == 'exit':
        break
    
    print(f'Connect to {HOST}')
    print('The Fabonnacci(n) when n = ' + outdata)
    s.sendall(outdata.encode('utf-8'))

    indata = s.recv(1024).decode('utf-8')
    print('The ans is ' + indata)

s.close()

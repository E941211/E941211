import socket

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

HOST = '192.168.137.73'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print('Server start at: %s:%s' % (HOST, PORT))
print('Waiting for connection...')

while True:
    conn, addr = s.accept()
    print('Connected by ' + str(addr))
    print(f'Add connection from {addr}')

    indata = conn.recv(1024).decode('utf-8')
    print(f'Received from {addr}: {indata}')

    try:
        input_number = int(indata)
        outdata = fibonacci(input_number)
        print(f'Send to {addr}: {outdata}')
        conn.sendall(str(outdata).encode('utf-8'))
    except ValueError:
        conn.sendall("Invalid input. Please send a number.".encode())

    print('Closed connection')
    conn.close()


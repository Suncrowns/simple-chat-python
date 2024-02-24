import socket
import threading
UDP_MAX_SIZe = 60000
members = []
def listen(server: socket.socket):
    while True:
        msg, addr = server.recvfrom(UDP_MAX_SIZe)
        if addr not in members:
            members.append(addr)
        else:
            print('\r\r' + msg.decode('utf-8') + '\n' + f'you: ', end='')
def connect(host: str = '127.0.0.1', port: int = 3000):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.connect((host, port))
    thread = threading.Thread(target=listen, args=(server,), daemon=True)
    thread.start()
    server.send('__join__'.encode('utf-8'))
    while True:
        msg = input('you: ')
        if msg == '/help':
            print('/members - get list of members\n/help - get list of commands\n/exit - exit chat')
        if msg == '/exit':
            server.send('__exit__'.encode('utf-8'))
            exit(0)
        if msg == '/members':
            msg = '__members__'
            server.send(msg.encode('utf-8'))
        else:
            server.send(msg.encode('utf-8'))
if __name__ == '__main__':
    print('welcome to chat')
    connect()

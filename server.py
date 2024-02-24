import socket

UDP_MAX_SIZe = 60000
def listen(host: str = '127.0.0.1', port: int = 3000):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print('server start work!')

    members = []
    while True:
        msg, addr = server.recvfrom(UDP_MAX_SIZe)
        if addr not in members:
            members.append(addr)
        client_id = addr[1]
        if msg.decode('utf-8') == '__join__':
            print(f'Client {client_id} joined chat')
            msg1 = 'client' + str(client_id) + ' joined chat'
            for m in members:
                if m == addr:
                    server.sendto(msg1.encode('utf-8'), m)
            continue
        if msg.decode('utf-8') == '__members__':
            addr1 = addr
            for m in members:
                if m != addr:
                    server.sendto((f'Client{m[1]}').encode('utf-8'), addr1)
            continue
        if msg.decode('utf-8') == '__exit__':
            for m in members:
                if m != addr:
                    server.sendto((f'Client{m[1]} diconnected').encode('utf-8'), m)
            members.remove(addr)
            continue
        msg = f'client{client_id}: {msg.decode("utf-8")}'
        for m in members:
            if m == addr:
                continue
            server.sendto(msg.encode('utf-8'), m)
if __name__ == '__main__':
    listen()

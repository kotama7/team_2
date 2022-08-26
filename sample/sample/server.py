import socket

server_ip = socket.gethostbyname(socket.gethostname())
server_address = (server_ip,6789)
max_size = 4096
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(server_address)
while True:
    data, client = server.recvfrom(max_size)
    print(data.decode('utf-8'))
    massage = input().encode('utf-8')
    with open(massage,'r',encoding='utf-8') as f:
        massage = f.read().encode('utf-8')
    server.sendto(massage,client)
    if not data or not massage:
        break
server.close()
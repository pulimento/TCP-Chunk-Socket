#!/usr/bin/python
# -*- coding: utf-8 -*-

server_ip = "127.0.0.1"
server_port = 9999
filename = "img.png"

import time
import socket

def split_chunks(input_string, size):
        length = len(input_string)
        chunknum = length / size
        list = []
        for i in range(0,length,size):
                list.append(input_string[i:i+size])
        return list 

f = open(filename,"rb")
filedata = f.read()
f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip,server_port))
print("Connected.")

file_array = split_chunks(filedata, 1000)
print("Chunks: "+str(len(file_array)))
time.sleep(1)
c = 0

for chunk in file_array:
	s.send(chunk)
	c += 1
	while 1:
		data = s.recv(1000)
		if data==chunk:
			break
time.sleep(4)
s.send("#")
print("Transmission complete!")

s.close()

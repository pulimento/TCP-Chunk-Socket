#!/usr/bin/python
# -*- coding: utf-8 -*-

listen_ip = "127.0.0.1"
listen_port = 9999
filename = "out.png"

import time
import socket

filedata = ""

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((listen_ip,listen_port))
s.listen(1)

while 1:
	conn,addr = s.accept()
	print("Connected.")
	while 1:
		data = conn.recv(1000)
		if len(data) > 0:
			if data=="#":
				conn.close()
				f = open(filename, "wb")
				f.write(filedata)
				f.close()
				print("Transmission complete!")
				conn.close()
				break
			else:
				filedata += data
				conn.send(data)

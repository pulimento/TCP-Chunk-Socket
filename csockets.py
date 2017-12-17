#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import socket

end_char = "#"

def split_chunks(input_string, size):
        length = len(input_string)
        chunknum = length / size
        list = []
        for i in range(0,length,size):
                list.append(input_string[i:i+size])
        return list 

def send_csocket(server_ip,server_port,chunksize,data):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip,server_port))
        data_array = split_chunks(data, chunksize)
        time.sleep(1)
        c = 0
        for chunk in data_array:
            s.send(chunk)
            c += 1
            while 1:
                data = s.recv(chunksize)
                if data==chunk:
                    break
        time.sleep(2)
        s.send(end_char)
        s.close()

def recv_csocket(listen_ip,listen_port,chunksize):
        outdata = ""
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((listen_ip,listen_port))
        s.listen(1)
        while 1:
            conn,addr = s.accept()
            while 1:
                data = conn.recv(chunksize)
                if len(data) > 0:
                    if data==end_char:
                        conn.close()
                        return outdata
                    else:
                        outdata += data
                        conn.send(data)

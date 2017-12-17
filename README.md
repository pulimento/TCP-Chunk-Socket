# TCP-Chunk-Socket
--- Python Module for transmitting large Files via TCP sockets---

Normally, Python sockets can only send and receive a limited amount of Data. When trying to send large files via a TCP socket, you will run into an error.

The module in this repository allows you to easily send large files via TCP.

Client example code:
~~~
import csockets as csk

csk.send_csocket("127.0.0.1",8080,1024,"Hello World")
~~~

Server example code:
~~~
import csockets as csk

print(csk.recv_csocket("127.0.0.1",8080,1024))
~~~

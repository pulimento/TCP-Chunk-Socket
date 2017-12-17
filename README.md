# TCP-Chunk-Socket
## Python Module for transmitting large Files via TCP sockets

Usually, Python sockets can only send and receive a limited amount of Data. With this simple Python module you can send very large files over a network with only a few lines of code.

### Client example code:
~~~
import csockets as csk

csk.send_csocket("127.0.0.1",8080,1024,"Hello World")
~~~

### Server example code:
~~~
import csockets as csk

print(csk.recv_csocket("127.0.0.1",8080,1024))
~~~

Obviously you have to replace the IP-Address ("127.0.0.1"), Port (8080), Chunksize (1024) and Data ("Hello World").

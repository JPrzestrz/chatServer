# Simple Python Chatting Server. 
## 1. Server & Client 
### 1.1 Server 
Project consists of two python apps: server and client. The server is responsible <br>
for handling connecting users and collect the messages. It uses threads in order <br>
to more efficiently handle incoming users. It collects messages from users and uses <br>
simple broadcast which means that it sends messages to all of the connected users <br>
Server allows to enter exit command in order to gracefully quit the server. <br> 
Server is by default hosted on the default 127.0.0.1 and port 5555. <br>

### 1.2 Client 
The client application allows to connect to the server application. When user first <br>
connects to the server, is requested to enter the username which later will be added <br>
to all of the incoming messages from given client. <br>

### 1.3 Requirements 
Python 3.0+<br>
running server and client app from the terminal<br> 
```python server.py```
```python client.py``` 
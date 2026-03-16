# 4.Execution_of_NetworkCommands
## REFNO:212225040325
## AIM :Use of Network commands in Real Time environment
## Software : Command Prompt And Network Protocol Analyzer
## Procedure: To do this EXPERIMENT- follows these steps:
<BR>
In this EXPERIMENT- students have to understand basic networking commands e.g cpdump, netstat, ifconfig, nslookup ,traceroute and also Capture ping and traceroute PDUs using a network protocol analyzer 
<BR>
All commands related to Network configuration which includes how to switch to privilege mode
<BR>
and normal mode and how to configure router interface and how to save this configuration to
<BR>
flash memory or permanent memory.
<BR>
This commands includes
<BR>
• Configuring the Router commands
<BR>
• General Commands to configure network
<BR>
• Privileged Mode commands of a router 
<BR>
• Router Processes & Statistics
<BR>
• IP Commands
<BR>
• Other IP Commands e.g. show ip route etc.
<BR>

## PROGRAM
server.py
```
import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 8000

server.bind((host, port))
server.listen(5)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Command received:", data)

    result = os.popen(data).read()

    if result == "":
        result = "Command executed but no output"

    conn.send(result.encode())

conn.close()
server.close()
```
client.py
```
import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 8000

server.bind((host, port))
server.listen(5)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Command received:", data)

    result = os.popen(data).read()

    if result == "":
        result = "Command executed but no output"

    conn.send(result.encode())

conn.close()
server.close()
```

## Output
1.ping
```
server
```
![alt text](<Screenshot 2026-03-16 090310.png>)
```
client
```
![alt text](<Screenshot 2026-03-16 090324 - Copy.png>)

Execution:
![alt text](<Screenshot 2026-03-16 090400.png>)

2.tracert

```
server
```
![alt text](<Screenshot 2026-03-16 090810.png>)
```
client
```
![alt text](<Screenshot 2026-03-16 090832.png>)

Execution
![alt text](<Screenshot 2026-03-16 090849.png>)

3.nslookup
```
server
```
![alt text](<Screenshot 2026-03-16 091152.png>)
```
client
```
![alt text](<Screenshot 2026-03-16 091204.png>)

Execution
![alt text](<Screenshot 2026-03-16 091222.png>)

4.netstat
```
server
```
![alt text](<Screenshot 2026-03-16 091549.png>)

```
client
```
![alt text](<Screenshot 2026-03-16 091600.png>)

Execution
![alt text](<Screenshot 2026-03-16 091616.png>)

## Result
Thus Execution of Network commands Performed 

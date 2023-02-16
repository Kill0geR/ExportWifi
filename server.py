import ExportWifi as wifi

server = wifi.WlanServer("127.0.0.1", 1111)
server.start()
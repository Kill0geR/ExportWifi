import ExportWifi as wifi

client = wifi.WlanClient("127.0.0.1", 1111)
client.start()
from vidstream import ScreenShareClient
import threading

ip = input("Please enter the IP of the device that you want to mirror (leave blank if you want this computer to be mirrored): ")

if ip == '':
    ip = '192.168.0.107'

sender = ScreenShareClient(ip, 9999)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != 's':
    continue

sender.stop_server()
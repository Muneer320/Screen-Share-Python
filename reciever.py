from vidstream import StreamingServer
import threading

reciever = StreamingServer('192.168.0.107', 9999)

t = threading.Thread(target=reciever.start_server)
t.start()

while input("") != 's':
    continue

reciever.stop_server()
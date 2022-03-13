import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
noggers = s.gethostbyname
print(noggers)
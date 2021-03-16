#

#! SOCKETY
#? Modul socket
# modul (knižnica) obsahujúca funkcie (metódy) socketov

import socket      

#? Vytvorenie socketu
# socket vytvorime pomocou metody "socket()", ktoru zavolame z modulu socket

sock = socket.socket()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0, fileno = None)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
sock.bind(("0.0.0.0", 80))
sock.listen(10)

(clientSock, clinetAddr) = sock.accept()        

sock.connect(("192.168.18.1", 80))     
sock.send()                         
sprava = sock.recv(1000)           
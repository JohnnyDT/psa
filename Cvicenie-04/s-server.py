#!/usr/bin/env python3

import socket
import json
from enum import IntEnum

class Sprava:
    def __init__(self, paOd, paKomu, paOperacia, paText):
        self.od = paOd
        self.komu = paKomu
        self.operacia = paOperacia
        self.text = paText

    @staticmethod
    def json_decoder(obj):
        return Sprava(obj['od'], obj['komu'], obj['operacia'], obj['text'])

class Operacia(IntEnum):        #dedenie
    LOGIN = 1
    EXIT = 2
    USERS = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind(("127.0.0.1", 9998))
sock.listen(10)

while True:
    
    (clientSock, clientAddr) = sock.accept()
    sprava = clientSock.recv(1500)

    jsonStr = sprava.decode()
    objekt = json.loads(jsonStr, object_hook=Sprava.json_decoder)

    print("Sprava od klienta [IP: {}, port: {}]: od: {}, komue: {}, text: {}".format(clientAddr[0], clientAddr[1], objekt.od, objekt.komu, objekt.text))
    clientSock.close()

sock.close()
#!/usr/bin/env python3

import socket
from enum import IntEnum
import json

class Sprava:
    def __init__(self, paOd, paKomu, paOperacia, paText):
        self.od = paOd
        self.komu = paKomu
        self.operacia = paOperacia
        self.text = paText

class Operacia(IntEnum):
    LOGIN = 1
    EXIT = 2
    USERS = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 9999))

sprava = Sprava("Martin", "Jozko", Operacia.LOGIN.value, "Ahoj cez socket z Pythonu")
jsonStr = json.dumps(sprava.__dict__)

sock.send(jsonStr.encode())

sock.close()

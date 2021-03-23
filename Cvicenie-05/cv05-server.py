#!/usr/bin/env python3

import socket
import json
import os
from enum import IntEnum
from threading import Thread

os.system("clear")

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

def spracuj_klienta(clientSock, clientAddr, pouzivatelia):
    while (True):   
        
        message = clientSock.recv(1500)
        jsonStr = message.decode()
        sprava = json.loads(jsonStr, object_hook=Sprava.json_decoder)

        if sprava.operacia == Operacia.LOGIN:
            pouzivatelia.append(sprava.od)
            print("Prihlasil sa pouzivatel {} [IP: {}, port: {}]".format(sprava.od, clientAddr[0], clientAddr[1]))
            print(pouzivatelia)
            continue

        if sprava.operacia == Operacia.EXIT:
            pouzivatelia.remove(sprava.od)
            print("Odhlasil sa pouzivatel {} [IP: {}, port: {}]".format(sprava.od, clientAddr[0], clientAddr[1]))
            print(pouzivatelia)
            clientSock.close()
            return

        if sprava.operacia == Operacia.USERS:
            odpoved = Sprava("", sprava.od, Operacia.USERS.value, pouzivatelia)
            jsonStr = json.dumps(odpoved.__dict__)
            clientSock.send(jsonStr.encode())
            continue

        print("Sprava od klienta [IP: {}, port: {}]: od: {}, komu: {}, text: {}".format(clientAddr[0], clientAddr[1], sprava.od, sprava.komu, sprava.text))

def prijmi_klienta(sock):
    while (True):
        (clientSock, clientAddr) = sock.accept()
        vlakno = Thread(target=spracuj_klienta, args=(clientSock, clientAddr, pouzivatelia, ))
        vlakno.start()

if __name__ == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.bind(("127.0.0.1", 9996))
    sock.listen(10)

    pouzivatelia = list()    

    vlakno = Thread(target=prijmi_klienta, args=(sock, ))
    vlakno.start()

    input()

    sock.close()
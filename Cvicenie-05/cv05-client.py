#!/usr/bin/env python3

import socket
import json
import os
from enum import IntEnum
from tkinter import *

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

def napoveda():
    print("\n***Napoveda***")
    print("  \\q - prikaz ukonci program")
    print("  \\l - prikaz vypise online pouzivatelov")
    print("  \\h - prikaz vypis napovedu")
    print(" Spravu odosielajte v tvare: nick:sprava")



def odosli():
    sprava = Sprava(nick, "Jozko", "", "Text z Buttonu")
    jsonStr = json.dumps(sprava.__dict__)
    sock.send(jsonStr.encode())

print("***Vita vas rogram CHAT v Pythone***")
nick = input("Zadaj svoj nick: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect(("127.0.0.1", 9996))

sprava = Sprava(nick, "", Operacia.LOGIN.value, "")
jsonStr = json.dumps(sprava.__dict__)
sock.send(jsonStr.encode())

napoveda()

hlavny = Tk()
hlavny.title("CHAT klient v Pythone")
hlavny.geometry("500x150")

ramik = Frame(hlavny)
ramik.pack()

popisok = Label(ramik, text="Klient")
popisok.pack()

tlacitko = Button(ramik, text="Odosli spravu", command=odosli)
tlacitko.pack()

hlavny.mainloop()


while (True):
    prikaz = input("Zadajte prikaz: ")

    if prikaz[0] == '\\':
        if prikaz[1] == 'h':
            napoveda()
            continue

        if prikaz[1] == 'q':
            sprava = Sprava(nick, "", Operacia.EXIT.value, "")
            jsonStr = json.dumps(sprava.__dict__)
            sock.send(jsonStr.encode())
            break

        if prikaz[1] == 'l':
            sprava = Sprava(nick, "", Operacia.USERS.value, "")
            jsonStr = json.dumps(sprava.__dict__)
            sock.send(jsonStr.encode())

            message = sock.recv(1500)
            objekt = json.loads(message.decode(), object_hook=Sprava.json_decoder)
            print("Zoznam pouzivatelov: ", objekt.text)
            continue

        
    vystup_prikazu = prikaz.split(":", 1)
    sprava = Sprava(nick, vystup_prikazu[0], "", vystup_prikazu[1])
    jsonStr = json.dumps(sprava.__dict__)
    sock.send(jsonStr.encode())

sock.close()
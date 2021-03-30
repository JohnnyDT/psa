import socket
import struct
import ipaddress

DNS_SERVER = "8.8.8.8"
DNS_PORT = 53

# hlavicka
transaction_id = socket.htons(0x1234)           # hton - host to network
flags = socket.htons(0x0100)
questions = socket.htons(0x0001)
answers = 0x0000
authority = 0x0000
additional = 0x000

# struktura, ktora obsahuje striktnu velkost 6 x 2B ---> h = 2B
header = struct.pack('hhhhhh', transaction_id, flags, questions, answers, authority, additional) 

otazka = "www.uniza.sk"
labels = otazka.split(".")                  # split vrati list

querry_body = b''

for label in labels:
    querry_body += bytes([len(label)])              
    
    for character in label:
        querry_body += bytes([ord(character)])
    
querry_body += bytes([0x00])

TYPE = socket.htons(0x0001)                 # TYPE A
CLASS = socket.htons(0x0001)                # INTERNET

querry_end = struct.pack('hh', TYPE, CLASS)

sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
sock.bind(("", 50000))

sock.sendto(header + querry_body + querry_end, (DNS_SERVER, DNS_PORT))

# ---------------------------------------------

response, addr = sock.recvfrom(1024)

resp_byte = response[3:4]           # 4. bajt


if (int.from_bytes(resp_byte, byteorder = "big") % 2 == 0):
    print(str(ipaddress.ip_address(response[-4:])))        # posledne 4 
else:
    print("Chyba v odpovedi.")

sock.close()
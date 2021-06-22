# Mikrotik

#! 158.193.152.64:2365         
#! 2R1
#! 192.168.1.21
#! https://158.193.152.77:33321
#! admin/class

#? PRIKAZY NA VYGENEROVANIE SELF CERTIFIKATU (v Mikrotiku)
#?
#? /certificate add name=LocalCA common-name=LocalCA key-usage=key-cert-sign,crl-sign
#? /certificate sign LocalCA
#? /certificate add name=REST common-name=192.168.1.21
#? /certificate sign REST ca=LocalCA
#? /ip service set www-ssl certificate=REST disabled=no

#* DOKUMENTACIA
#* 
#* Mikrotik REST API:
#* https://help.mikrotik.com/docs/display/ROS/REST+API
#*
#* Kniznica requests:
#* https://docs.python-requests.org/

# ------------------------------------------------------------------------------------------------------------------

import requests

ip = "158.193.152.77"
port = "33321"
meno = "admin"
heslo = "class"

def a():
    prikaz = "ip/address"
    ziadost = requests.get("https://{}:{}/rest/{}".format(ip, port, prikaz), auth = (meno, heslo), verify = False)
    print(ziadost.status_code)
    print(ziadost.text)
    print(ziadost.json())

def b():
    prikaz = "interface"
    ziadost = requests.get("https://{}:{}/rest/{}".format(ip, port, prikaz), auth = (meno, heslo), verify = False)
    if ziadost.status_code == 200 :
        for r in ziadost.json():
            
            ena = ("enable" if r['disabled'] == "false" else "dis")
            run = ("up" if r['running'] == "true" else "down")
            print("Nazov: {} {} {}".format(r['name'], ena, run))
    else:
        print("\nKod: {}\nSprava: {}\nPopis: {}\n".format(ziadost.json()['error'], ziadost.json()['message'], ziadost.json()['detail']))

def c():
    prikaz = "ip/address"
    telo =  {
            'address' : '10.1.1.1/24',
            'interface' : 'ether3' 
            }
    ziadost = requests.put("https://{}:{}/rest/{}".format(ip, port, prikaz), auth = (meno, heslo), verify = False, json = telo)
    print(ziadost.status_code)
    print(ziadost.json())

def d():
    prikaz = "ip/address/*2"
    telo =  {
            'address' : '10.4.1.1/24'
            }
    ziadost = requests.patch("https://{}:{}/rest/{}".format(ip, port, prikaz), auth = (meno, heslo), verify = False, json = telo)
    print(ziadost.status_code)
    print(ziadost.json())

def e():
    prikaz = "ip/address/*2"
    ziadost = requests.delete("https://{}:{}/rest/{}".format(ip, port, prikaz), auth = (meno, heslo), verify = False, json = telo)
    print(ziadost.status_code)
    print(ziadost.json())

def f():
    id = ""
    prikaz = "ip/address"
    ziadost = requests.get("https://{}:{}/rest/{}".format(ip, port, prikaz), auth = (meno, heslo), verify = False)
    print(ziadost.status_code)
    for r in ziadost.json():
        if r['interface'] == 'ether3':
            id = r['.id']
            print("ID zaznamu: " + id)

    prikaz = "ip/address/" + id
    ziadost = requests.delete("https://{}:{}/rest/{}".format(ip, port, prikaz), auth = (meno, heslo), verify = False, json = telo)
    print(ziadost.status_code)
    print(ziadost.json())
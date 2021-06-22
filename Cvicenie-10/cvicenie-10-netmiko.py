from netmiko import ConnectHandler

Cisco = {
    'device_type' : 'cisco_ios',
    'host' : '158.193.152.121',
    'port' : 22231,
    'username' : 'admin',
    'password' : 'class',
}

pripojenie = ConnectHandler(**Cisco)

loop = [
    'int lo{}'.format(4),
    'ip add {} {}\n'.format("2.1.1.1", "255.255.255.255")
]

vystup = pripojenie.send_config_set(loop)
print(vystup)

print('*********************************')

vystup = pripojenie.send_command('sh ip int br')
print(vystup)

pripojenie.disconnect()
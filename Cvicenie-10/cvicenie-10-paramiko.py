# Router - SSH
#? https://www.gns3.com/
#? https://www.paramiko.org/

# 158.193.152.64:2171       - telnet
# 192.168.1.31 255.255.255.0
# 158.193.152.121:22231     - SSH

from paramiko import SSHClient, AutoAddPolicy
import time

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('158.193.152.121', port = 22231, username = 'admin', password = 'class')

conn = client.invoke_shell()
conn.send('conf t\n')
time.sleep(0.5)
conn.send('int lo2\n')
time.sleep(0.5)
conn.send('ip add {} {}\n'.format("1.1.1.1", "255.255.255.255"))
time.sleep(0.5)
conn.send('end\n')
time.sleep(0.5)

# stdin, stdout, stderr = client.exec_command('sh ip int brief')
# zoznam = list()
# 
# for riadok in stdout:
#     zoznam.append(riadok.strip('\n').strip('\r'))
# 
# print(zoznam[2].split(' '))
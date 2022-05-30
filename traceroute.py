import re
import socket

open_host = open('/home/saisri/scripts/traceroute.txt', 'r')
traceroute = open_host.read()

ip = []
iptoname = {}
for line in traceroute.splitlines():
    try:
         ipPattern = re.search(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', line)
         ip.append(ipPattern.group())
    except AttributeError:
         continue
for i in ip:
    try:
         name = socket.gethostbyaddr(i)[0]
         iptoname[i] = name
    except socket.herror:
         iptoname[i]= "Host not found"

for line in traceroute.splitlines():
    key = line.split()[-1]
    try:
        print line.replace(key, iptoname[key])
    except KeyError:
        continue

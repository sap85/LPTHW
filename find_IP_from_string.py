import re
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 192.168.1.1 sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis 58.23.14.12 nostrud exercitation ullamco laboris nisi ut aliquip
ex ea commodo consequat. 255.255.255.1 Duis aute irure dolor in reprehenderit
in voluptate velit esse 192.168.256.0 cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, 10.0.0.10
sunt in culpa qui officia deserunt mollit anim id est laborum 20.25.a.10"""
#print(text)

ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', text )
print(ip)

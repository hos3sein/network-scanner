from scapy.all import *

ip = IP()

# ip.show()

#its for fucking check

# destination ip address
target_ip = '192.168.1.1/24'

# create arp packet
arp = ARP(pdst = target_ip)

# create the ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting

ether = Ether(dst = "ff:ff:ff:ff:ff:ff")

# stack them
packet = ether/arp

# now we send the packets in layer 2

res = srp(packet , timeout = 3)[0]


clients = []

for sent , recieved in res:
	clients.append({'ip': received.psrc, 'mac': received.hwsrc})


# now we just need to print the resault to see the devicess

print('available devices')
for client in clients:
	print("{:16}    {}".format(client['ip'], client['mac']))

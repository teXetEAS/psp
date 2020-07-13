import netfilterqueue
import scapy.all as scapy

def procPack(packet):
	scapyPack = scapy.IP(packet.get_payload())
	if scapyPack.haslayer(scapy.Raw):
		print(scapyPack.show())
		
	packet.accept()
	
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, procPack)
queue.run()

#sudo iptables --flus
#50 эпизод

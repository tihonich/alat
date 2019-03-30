'''    Simple socket server using threads
'''
import socket
import subprocess
import sys
import array as arr
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

HOST = ''   # Symbolic name, meaning all available interfaces

# Ask for input

# Check what time it is
t1 = datetime.now()
print (t1)

def create_socket(port_number):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind socket to local host and port
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', port_number))
    server_socket.listen(1)
    return server_socket

port_number = [int(i) for i in raw_input('Input ports: ').split()]
print port_number

port_array = arr.array('i', port_number)
print (port_array[:])

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s8 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s9 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to local host and port

socket_list = []

for port_number in (port_array[:]):
    try:
        socket_list.append(create_socket(port_number))
    except Exception: 
        pass 		
print 'Sockets bind complete'
#Start listening on socket
s1.listen(10)
s2.listen(10)
s3.listen(10)
s4.listen(10)
s5.listen(10)
s6.listen(10)
s7.listen(10)
s8.listen(10)
s9.listen(10)
s10.listen(10)

print 'Sockets now listening'
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s1.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s1.close()
while 2:
    #wait to accept a connection - blocking call
    conn, addr = s2.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s2.close()
while 3:
    #wait to accept a connection - blocking call
    conn, addr = s3.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s3.close()

while 4:
    #wait to accept a connection - blocking call
    conn, addr = s4.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s4.close()

while 5:
    #wait to accept a connection - blocking call
    conn, addr = s5.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s5.close()

while 6:
    #wait to accept a connection - blocking call
    conn, addr = s6.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s6.close()

while 7:
    #wait to accept a connection - blocking call
    conn, addr = s7.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s7.close()

while 8:
    #wait to accept a connection - blocking call
    conn, addr = s8.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s8.close()

while 9:
    #wait to accept a connection - blocking call
    conn, addr = s9.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s9.close()

while 10:
    #wait to accept a connection - blocking call
    conn, addr = s10.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s10.close()
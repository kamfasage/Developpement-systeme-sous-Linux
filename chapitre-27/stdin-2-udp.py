#! /usr/bin/python
from __future__ import print_function
import os
import socket
import sys

def lecture_arguments():
	server_name = "localhost"
	service_name = "2000"
	sys.argv.pop(0)
	while len(sys.argv) > 0:
		if sys.argv[0] == "-a":
			sys.argv.pop(0)
			server_name = sys.argv[0]
			sys.argv.pop(0)
			continue
		if sys.argv[0] == "-p":
			sys.argv.pop(0)
			service_name = sys.argv[0]
			sys.argv.pop(0)
			continue
		print("Unkown option:", sys.argv[0])
		sys.exit(1)
	try:
		result = socket.getaddrinfo(server_name, service_name,
			 socket.AF_INET, 0, 0)
	except:
		print("Invalid host or service name")
		sys.exit(1)
	return result


result = lecture_arguments()
(family, socktype, proto, canon, sockaddr) = result[0]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
	buffer =  os.read(sys.stdin.fileno(), 4096)
	if buffer == "":
		break
	sock.sendto(buffer, sockaddr)


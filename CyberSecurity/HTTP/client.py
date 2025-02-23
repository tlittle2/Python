#!/usr/bin/env

import socket
import datetime
import sys

if len( sys.argv ) <=1:
	print("Please specify your host and the page you want")
	exit(0)
	
host = sys.argv[1]
port= int(sys.argv[2])
if len(sys.argv) < 4:
	page= '/'
else:
	page= sys.argv[3]
	
	

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect(( host,port ))
	
	http_request= "GET " + str(page) + " HTTP/1.0\r\n"
	http_request+= "HOST: " + str(host) + "\r\n"
	http_request+= "\r\n"
	
	print("HTTP Request:")
	print(http_request)
	s.sendall( str.encode( http_request ) )
	response_buffer= b'' 
	
	while True:
		data= s.recv(1024)
		response_buffer+=data
		if len(data) == 0:
			break
			
	print("HTTP Response: ")
	print(response_buffer.decode('utf-8', "ignore"))
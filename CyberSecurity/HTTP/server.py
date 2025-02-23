#!/usr/bin/env python3

import socket
import sys
import datetime
import os

HOST = '0.0.0.0'
PORT= 37301

def make_header(response, payload):
	header = "HTTP/1.0 {0}\r\n".format(response)
	header+= "Date: " + str(datetime.datetime.utcnow().strftime('%a %d %b %Y %H:%M:%S GMT '))
	header+= "Server: Cybersecurity-Lab HTTP\r\n"
	header+= "Content-Length: {0}\r\n".format(len(payload))
	header+= "Connection : close\r\n"
	header+= "Content-Type: text/html\r\n"
	header+= "\r\n" #BLANK LINE IS IMPORTANT
	
	return header + payload

def process_request(conn):
	buffer= ""
	while True:
		data = conn.recv(1024)
		if not data:
			break
		
		buffer+= data.decode('utf-8', "ignore")
		
		#check if request is complete
		if buffer.endswith("\r\n\r\n"):
			break
			
			
	#parse the request
	response= parse_request(buffer)
	if not response:
		response = respond_404()
		
		
	#send a response
	print("Response is ")
	print(response)
	conn.sendall(str.encode(response))


def respond_404():
	html= '''
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
<hr>
<address>CS373 Lab HTTP-Server at {0} Port 80</address>
</body></html>
'''.format(HOST)

	return make_header("404 Not Found", html)



def parse_request(buffer):
	#check if a GET request
	
	if not buffer.startswith("GET"):
		return False
		
	(method, uri, prot) = buffer.split(' ', 2)
	
	# find uri on disk
	if uri.endswith('/'):
		uri += "index.html"
	
	filepath= os.getcwd() + uri
	print("Looking for file " + str(filepath))
	
	if os.path.isfile(filepath):
		#found the file
		with open(filepath) as fd:
			return make_header("200 OK", fd.read())
	else:
		print("File not found")
		return False


def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		my_port= PORT

		while True:
			try:
				s.bind((HOST, my_port))
				break
				
			except Exception as e:
				print(e, " trying next port...")
				my_port+=1
		s.listen();
		print("Patiently waiting on " + str(HOST) + " and " + str(my_port))
		
		while True:
			print("Waiting for next connection...")
			conn, addr= s.accept()
			print("Got connected with " + str(addr))
			
			try:
				with conn:
					process_request(conn)
				
			except Exception as e:
				print("Error: " + str(e))
			
			print("Done with connection from " + str(addr))
				
				

if __name__ == "__main__":
	main()

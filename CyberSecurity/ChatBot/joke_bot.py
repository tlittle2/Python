import sys
import os
import socket
import pyjokes




def main( HOST, PORT, USERNAME ):
    with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as s:  
        s.connect( (HOST,int(PORT)) )
		





if __name__=="__main__":
    if len(sys.argv) < 4:
        print("Usage: chat_client.py HOSTNAME PORT USERNAME")
    else:
        main( sys.argv[1], sys.argv[2], sys.argv[3] )
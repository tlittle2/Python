import sys
import os
import socket







def main():





if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: chat_client.py HOSTNAME PORT USERNAME")
    else:
        main( sys.argv[1], sys.argv[2], sys.argv[3] )
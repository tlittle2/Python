#!/usr/bin/env python3

import socket
import time
import sys
import threading
import queue
#import gnupg
import json

from chat_server_skeleton import ClientClosedConnection, read_lines, reader_thread


recv_q = queue.Queue(10)  # initialize recv message queue
#gpg = gnupg.GPG(homedir="/home/tlittle2/.gnupg/")


def process_received_message_client(lines):
    #print(lines)
    assert(lines[0] == "BEGIN")
    assert(lines[-1] == "END")
    msg = json.loads(lines[1])
    if msg['type'] == "hello":
        print(msg['name'] + " has joined the chatroom")

    elif msg['type'] == "broadcast":
        print("{0} has sent a broadcast message saying {1} ".format(msg['user'], msg['message']))

    elif msg['type'] == "request":
        print("{0} is requesting a private key from {1} ".format(
            msg['user'], msg['receiver']))

    elif msg['type'] == "private":
        print("{0} is sending a private message to {1}".format(
            msg['user'], msg['receiver']))
    #print(msg)


def send_hello(sock, username):
    msg = {}
    msg['type'] = "hello"
    msg['name'] = username
    send_message(sock, msg)  # send over TCP


def send_hello_ack(sock, username):
    msg = {}
    msg['type'] = "hello_ack"  # type of message
    msg['name'] = username  # tell everyone our name
    send_message(sock, msg)


def send_private(sock, username):
    msg = {}
    msg["type"] = "private"  # type of message
    msg['name'] = username  # tell everyone our name
    send_message(sock, msg)


def send_request(sock, username):
    msg = {}
    msg["type"] = "request"  # type of message
    msg['name'] = username  # tell everyone our name
    send_message(sock, msg)


def send_goodbye(sock, username):
    msg = {}
    msg["type"] = "goodbye"  # type of message
    msg['name'] = username  # tell everyone our name
    send_message(sock, msg)


def send_goodbye_ack(sock, username):
    msg = {}
    msg["type"] = "goodbye_ack"  # type of message
    msg['name'] = username  # tell everyone our name
    send_message(sock, msg)  # send over TC


def send_message(sock, msg):
    msg_json = json.dumps(msg)
    msg_json = "BEGIN\n{0}\nEND\n".format(msg_json)
    # print(msg)
    #print("inside send_message()")
    sock.sendall(str.encode(msg_json))  # send over TCP


def tell_joke(conn):
    while True:
        time.sleep(2)
        send_message(
            conn, {'message': "this is a fake joke", 'type': "broadcast"})


def recvThread(socket, user):
    while True:
        # get next message
        msg = recv_q.get()
        # if anyone says hello, respond
        print(msg)
        if msg['type'] == "hello":
            print("{0} has joined the chatroom".format(msg['name']))
            send_hello_ack(socket, user)
        # if we get a hello_ack, print it out to the user
        elif msg['type'] == "hello_ack":
            print("{0} is in the chatroom".format(msg['name']))

        elif msg['type'] == "goodbye":
            print("{0} has left the chatroom".format(msg['name']))
            send_goodbye_ack(socket, user)
        # if we get a hello_ack, print it out to the user

        elif msg['type'] == "private":
            print(msg['receiver'])
            receiver = msg['receiver']
            msg = {}
            msg['type'] = "private"
            msg['name'] = user
            #msg['message'] = private_message
            send_message(socket, msg)
            print("{0} is sending a private message to {1}".format(
                msg['name'], receiver))

        elif msg['type'] == "request":
            msg = {}
            msg['type'] = "request"
            msg['name'] = user
            msg['message'] = "{0} is receiving a request".format(user)
            print("{0} receiving a request for a public key".format(
                msg['name']))

        else:
            msg = {}
            msg['type'] = "broadcast"
            msg['name'] = user
            msg['message']
            send_message(socket, msg)


def makeNewMessage(socket, user):
    print("Message type (broadcast, private, or request?):")
    type = sys.stdin.readline().rstrip()
    # print(type)

    if type == "private" or type == "request":
        receiver = input("recipient:")
        message = input("message: ")
        send_message(socket, {
                     "user": user, "receiver": receiver, "type": type, "message": message})

    elif type == "broadcast":

        message = input("message: ")
        send_message(
            socket, {"user": user, "type": type, "message": message})


def main(HOST, PORT, USERNAME):
    #print("WE HAVE STARTED MAIN()")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        # create reader thread
        tr = threading.Thread(target=reader_thread, args=(
            s, process_received_message_client,))
        tr.daemon = True
        tr.start()

        #tj = threading.Thread(target=tell_joke, args=(s,) )
        #tj.daemon = True
        # tj.start()

        # start the chat protocol
        send_hello(s, USERNAME)

        while True:
            recv_Thread = threading.Thread(
                target=recvThread, args=(s, USERNAME,))
            recv_Thread.daemon = True
            recv_Thread.start()
            for line in sys.stdin:
                if line.rstrip() == "NEW MESSAGE":
                    makeNewMessage(s, USERNAME)

                #send_goodbye(s, USERNAME)
        s.close()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: chat_client.py HOSTNAME PORT USERNAME")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])

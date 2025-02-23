#!/usr/bin/env python3

PORT_START = 37301
HOST = '0.0.0.0'  # all network interfaces

import socket
import threading
import queue


list_of_queues = []

class ClientClosedConnection(Exception):
    ''' empty class for our custom exception '''
    pass

def read_lines(conn):
    """ read from a socket, and return an array of strings """
    buff = ''
    while True:
        data = conn.recv(1024)
        if not data:
            #break  # got end of message
            raise ClientClosedConnection('client closed connection')
        buff += data.decode('utf-8',"ignore")
        if buff.endswith("\n"):
            break
    #print("RECV: {0}".format(buff))
    buff.replace("\r","")  # remove all "\r" chars
    return buff.split("\n")



def reader_thread(conn, process):
    try:
        lines = []
        while True:
#            lines.extend( read_lines(conn) )
            # remove all blank lines
#            for i in range(len(lines)):
#                if lines[i] == '':
#                    del lines[i]
#            lines = [(x) for x in lines if x != '']
            for line in read_lines(conn):
                if line != '':
                    lines.append(line)

            while True:
                msg_start = None
                msg_end = None
                # looking for a "BEGIN"
                #print("reader_thread() lines={0}".format(lines))
                for i in range(len(lines)):
                    if lines[i] == "BEGIN":
                        #print("got begin at i={0}".format(i))
                        msg_start = i
                        break
                if msg_start is not None:
                    for i in range(msg_start,len(lines)):
                        if lines[i] == "END":
                            #print("got end at i={0}".format(i))
                            msg_end = i
                            break
                if msg_start is not None and msg_end is not None:
                    process(lines[msg_start:msg_end+1])
                    #  remove message from lines
                    # also throw away everything before begin
                    del lines[0:msg_end+1] 
                else:
                    break
    except ClientClosedConnection as e:
        print(e)

def process_received_message_server(message_lines):
    ''' broadcast to all clients ''' 
    for q in list_of_queues:
        q.put( message_lines, False)  # non-blocking put


def writer_thread(conn,que):
    while True:
        msg_to_send = que.get()  #block until we get a message to send
        msg_data = "\n".join( msg_to_send ) + "\n"

        conn.sendall( str.encode( msg_data ) )

def main():
    # make socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # find open port
    PORT = PORT_START
    while PORT < PORT_START+20:  # check 20 ports, then give up
        try:
            s.bind( (HOST,PORT) )
            print("Server bound to port {0}".format(PORT))
            break
        except:
            PORT+=1
    #got an open port
    try:
        s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen()
        while True:
            # wait for connection
            conn, addr = s.accept()
            print("New connection from {0}".format(addr))
            # create queue for this client
            q = queue.Queue(10)
            list_of_queues.append( q )
            # create threads to handle connection to client
            # reader thread
            tr = threading.Thread(target=reader_thread, args=(conn,process_received_message_server,) )
            tr.daemon = True  # clean up after thread ends
            tr.start()
            # writer thread
            tw = threading.Thread(target=writer_thread, args=(conn,q,) )
            tw.daemon = True
            tw.start()

        
    finally:
        s.shutdown(socket.SHUT_WR)  # clean up the socket
        s.close()


if __name__=="__main__":
    main()

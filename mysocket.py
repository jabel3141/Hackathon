#from cueballfinder import CueBallFinder
from cueballfinder2 import CueBallFinder
import cv2
import numpy as np
import socket
import sys
from threading import *




def main():
    pipeline = CueBallFinder()
    cap = cv2.VideoCapture('testVid.avi')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret):
            # import pdb;pdb.set_trace()
            output= pipeline.process(frame)
            cv2.imshow('frame',frame)
            #print (output)
            coordinates = output
            #print(coordinates)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


 
# HOST = '130.215.11.31'   # Symbolic name, meaning all available interfaces
# PORT = 5555  # Arbitrary non-privileged port
 
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except(socket.error, msg):
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit();
 
print('Socket Created')
 
host = '130.215.11.31'
port = 5555
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((host, port))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(10)
print('Socket now listening')
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
 
try :
    #Set the whole string
    #s.sendall(message)

    while 1:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))
         
        data = conn.recv(1024)
        reply = b'OK...' + data
        if not data: 
            break
         
        conn.sendall(reply)
	 
    conn.close()
    s.close()
except socket.error:
    #Send failed
    print('Send failed')
    sys.exit()
 
print('Message send successfully')


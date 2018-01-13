# #from cueballfinder import CueBallFinder
# from cueballfinder2 import CueBallFinder
# import cv2
# import numpy as np
# import sys
# from flask import Flask, render_template, request, redirect, Response
# import random, json

# app = Flask(__name__)

# coordinates = [400,500];

# @app.route("/")
# def output():
#     return render_template("index.html")

# @app.route("/getCoordinates")
# def send():
#     print(coordinates)
#     values = json.dumps(coordinates)
#     print(values)
#     return values

# @app.route('/receiver', methods = ['POST'])
# def main():
#     # cue =  CueBallFinder();
#     #
#     #
#     # output = cue.process(img)
#     # # for contour in output:
#     # #     (x,y,w,h) = cv2.boundingRect(contour)
#     # #     cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
#     #
#     # cv2.imshow("image", img)
#     # cv2.waitKey(0)



#     pipeline = CueBallFinder()
#     cap = cv2.VideoCapture('testVid.avi')
#     while(cap.isOpened()):
#         ret, frame = cap.read()
#         if(ret):
#             # import pdb;pdb.set_trace()
#             output= pipeline.process(frame)
#             cv2.imshow('frame',frame)
#             #print (output)
#             coordinates = output
#             #print(coordinates)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#     cap.release()
#     cv2.destroyAllWindows()


# # def worker():
# #     # read json + reply

# #     data = request.get_json()
# #     result = ''
# #     print(data)
    

# #     for item in data:
# #         print(item)
# #         # loop over every row
# #         if(item == 'x'):
# #             result += 'x ' + str(data.get(item)) + '\n'
# #         else:
# #             result +=  'y ' + str(data.get(item))  + '\n'

# #     return result


# if __name__ == "__main__":
#     app.run(host="130.215.11.31", debug=True)



'''
    Simple socket server using threads
'''
 
import socket
import sys
 
HOST = '130.215.11.31'   # Symbolic name, meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    
     
s.close()



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
#from cueballfinder import CueBallFinder
from cueballfinder2 import CueBallFinder
import cv2
import numpy as np
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json
import socket

app = Flask(__name__)

coordinates = []

@app.route("/")
def output():
    return render_template("index.html")

@app.route("/getCoordinates")
def send():
    global coordinates
    print(coordinates)
    values = json.dumps(coordinates)
    print(values)
    return values


@app.route('/receiver', methods = ['POST'])
def main():
    # cue =  CueBallFinder();
    #
    #
    # output = cue.process(img)
    # # for contour in output:
    # #     (x,y,w,h) = cv2.boundingRect(contour)
    # #     cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
    #
    # cv2.imshow("image", img)
    # cv2.waitKey(0)

    global coordinates

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
            print(coordinates)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


# def worker():
#     # read json + reply

#     data = request.get_json()
#     result = ''
#     print(data)
    

#     for item in data:
#         print(item)
#         # loop over every row
#         if(item == 'x'):
#             result += 'x ' + str(data.get(item)) + '\n'
#         else:
#             result +=  'y ' + str(data.get(item))  + '\n'

#     return result

if __name__ == "__main__":
    app.run(host="130.215.11.31", debug=True, threaded=True)



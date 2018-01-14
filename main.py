#from cueballfinder import CueBallFinder
from cueballfinder2 import CueBallFinder
from yellowballfinder import YellowFinder
from redballfinder import RedFinder
from darkredballfinder import DarkRedFinder
from blueballfinder import BlueFinder
from greenballfinder import GreenFinder
from purpleballfinder import PurpleFinder
from distance import CornerDistance
import cv2
import numpy as np
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json, math
import socket

app = Flask(__name__)

cueCoords = []
redCoords = []
yellowCoords = []

@app.route("/")
def output():
    return render_template("index.html")

@app.route("/getCoordinates")
def send():
    global cueCoords
    global yellowCoords
    global redCoords
    global brownCoords
    global blueCoords
    global greenCoords
    global purpleCoords
    #cue, yellow, red, brown, blue, green, purple
    coordinates = [cueCoords, yellowCoords, redCoords, brownCoords]
    print(coordinates)
    values = json.dumps(coordinates)
    print(values)
    return values


@app.route('/receiver', methods = ['POST'])
def main():
    global cueCoords
    global yellowCoords
    global redCoords
    global brownCoords
    global blueCoords
    global greenCoords
    global purpleCoords

    pipeline = CueBallFinder()

    yellowBall = YellowFinder()
    redBall = RedFinder()
    brownBall = DarkRedFinder()
    blueBall = BlueFinder()
    greenBall = GreenFinder()
    purpleBall = PurpleFinder()
    cornerDistance = CornerDistance()
    cap = cv2.VideoCapture(1)
    leftCorner =[]

    while cap.isOpened():
        ret, frame = cap.read()
        if(ret):
            corners = cornerDistance.process(frame)
            #print(corners)
            # cv2.imshow('frame', frame)
            cornerDist = math.sqrt(math.pow(corners[0][0]+ corners[1][0], 2)+math.pow(corners[0][1]+corners[1][1],2))
            if corners[0][0]<corners[1][0]:
                leftCorner = corners[0]
            else:
                leftCorner = corners[1]
            break


    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret):
            # import pdb;pdb.set_trace()
            output= pipeline.process(frame)
            oneBall = yellowBall.process(frame)
            threeBall = redBall.process(frame)
            sevenBall = brownBall.process(frame)
            twoBall = blueBall.process(frame)
            sixBall = greenBall.process(frame)
            fourBall = purpleBall.process(frame)
            cv2.imshow('frame',frame)
            #print (output)

            if(len(output) != 0):
                cueCoords = [output[0]-leftCorner[0],output[1]-leftCorner[1]]
            if(len(oneBall) != 0):
                yellowCoords = [oneBall[0]-leftCorner[0],oneBall[1]-leftCorner[1]]
            if(len(threeBall) != 0):
                redCoords = [threeBall[0]-leftCorner[0],threeBall[1]-leftCorner[1]]
            if(len(sevenBall) != 0):
                brownCoords = [sevenBall[0]-leftCorner[0],sevenBall[1]-leftCorner[1]]
            if(len(twoBall) != 0):
                brownCoords = [twoBall[0]-leftCorner[0],twoBall[1]-leftCorner[1]]
            if(len(sixBall) != 0):
                brownCoords = [sixBall[0]-leftCorner[0],sixBall[1]-leftCorner[1]]
            if(len(fourBall) != 0):
                brownCoords = [fourBall[0]-leftCorner[0],fourBall[1]-leftCorner[1]]

            #print (cueCoords)
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

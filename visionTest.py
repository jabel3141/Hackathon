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
import math

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
    yellowBall = YellowFinder()
    redBall = RedFinder()
    darkredBall = DarkRedFinder()
    blueBall = BlueFinder()
    greenBall = GreenFinder()
    purpleBall = PurpleFinder()
    cornerDistance = CornerDistance()
    cap = cv2.VideoCapture(0)
    leftCorner =[]

    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if ret:
    #         corners = cornerDistance.process(frame)
    #         #print(corners)
    #         # cv2.imshow('frame', frame)
    #         cornerDist = math.sqrt(math.pow(corners[0][0]+ corners[1][0], 2)+math.pow(corners[0][1]+corners[1][1],2))
    #         if corners[0][0]<corners[1][0]:
    #             leftCorner = corners[0]
    #         else:
    #             leftCorner = corners[1]
    #
    #         break

    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret):
            # import pdb;pdb.set_trace()
            output= pipeline.process(frame)
            oneBall = yellowBall.process(frame)
            threeBall = redBall.process(frame)
            darkred = darkredBall.process(frame)
            blueball = blueBall.process(frame)
            greenball = greenBall.process(frame)
            purpleball = purpleBall.process(frame)
            cv2.imshow('frame',frame)
            #print (output)
            #print(oneBall)
            #print(threeBall)
            # if(len(output) != 0):
            #     coordinates = [output[0]-leftCorner[0],output[1]-leftCorner[1]]
            # #print (coordinates)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

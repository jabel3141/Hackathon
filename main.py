#from cueballfinder import CueBallFinder
from cueballfinder2 import CueBallFinder
import cv2
import numpy as np
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



    pipeline = CueBallFinder()
    cap = cv2.VideoCapture('testVid.avi')
    while(cap.isOpened()):
        ret, frame = cap.read()
        # import pdb;pdb.set_trace()
        output= pipeline.process(frame)
        cv2.imshow('frame',frame)
        print output
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__=='__main__':
    while True:
        main()

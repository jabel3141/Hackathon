# Billiard Ball  Tracking

## Github
https://github.com/jabel3141/Hackathon

## Youtube Video
https://www.youtube.com/watch?v=TJchry_SY3Q

## Team Members
Jason Abel
Nikhil Castelino
James Corse
Rayyan Khan 
Thomas Hagen

## Project Description
This project tracks billiard balls on a table using a camera. We then take this information and create
an image of a billiards table and balls using p5 libraries. Finally we display this image onto the billiards table
using a projector highlighting the balls and the ball's movements on a table. This project uses 8 threads
in order for it to track 7 billiard balls at the same time and create an image for it. p5 libraries were used to create images
and OpenCV was used for ball tracking

## Equipment:
- Camera
- Projector
- Mini Billiards set (includes table, balls, cue sticks, etc.)

## index.html
- Contains the html code for the webpage
- Uses p5 librabires to create the billiard table and balls

## blueballfinder.py
- Used to track the blue ball on the billiard table
- Tracks balls using OpenCV
- Returns the x and y coordinates of the ball

## cueballfinder2.py
- Used to track the cue ball on the billiard table
- Tracks balls using OpenCV
- Returns the x and y coordinates of the ball

## darkredballfinder.py
- Used to track the brown ball on the billiard table
- Tracks balls using OpenCV
- Returns the x and y coordinates of the ball

## distance.py
- Used to measure the table length
- Measured using OpenCV
- Returns the x and y coordinates of two corners

## greenballfinder.py
- Used to track the green ball on the billiard table
- Tracks balls using OpenCV
- Returns the x and y coordinates of the ball

## main.py
- Runs the server on flask
- Contains all the POST and GET requests made by index.html
- Communicates with all the ballfinder.py files

## purpleballfinder.py
- Used to track the purple ball on the billiard table
- Tracks balls using OpenCV
- Returns the x and y coordinates of the ball

## redballfinder.py
- Used to track the red ball on the billiard table
- Tracks balls using OpenCV
- Returns the x and y coordinates of the ball

## visionTest.py
- Used to test the ballfinder.py files

## yellowballfinder.py
- Used to track the yellow ball on the billiard table
- Tracks balls using OpenCV
- Returns the x and y coordinates of the ball
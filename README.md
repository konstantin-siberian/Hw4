# Hw4
Konstantin Turubanov
Variant A: Follow the line by light sensor.

Goal: make sure EV3 is able to follow the colored line

Work process:
-I had general lack of understanding and partially solved it by reading.

1. Quickly read suggested tutorials in moodle
2. Assemble relevant configuration with color sensor looking down (for my case purpose)
2. Put microUSB card inside the robot
3. Set up SSH connection, following the guide: http://www.ev3dev.org/docs/getting-started/
4. (I had to input IP in putty, because I have Windows 10, ev3dev does not work)
robot@ev3dev:~$ fortune
Clothes make the man.  Naked people have little or no influence on society.
                -- Mark Twain
5. pip install python-ev3dev-1.0.0.tar.gz (downloaded from https://pypi.python.org/pypi/python-ev3dev)
6. remote host adjustment
7. robot@ev3dev:~$ python3 hw4_v1.py
8. http://www.legoengineering.com/inside-a-two-step-simple-line-follower/
Implementing algorithm. (If we went to far left/right, we have to comeback)

My result values are not the best, but it kinda works ;)
First, I calibrated the sensor in respect to intensity values.
1 corresponded to black surface;
10 to the line edge
17 to the center of the line.
And accelerated corresponding wheels to make sure the robot following the line. (Initially I placed it to the right from the line).

P.S. I sent you the video in telegram

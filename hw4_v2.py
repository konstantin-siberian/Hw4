from ev3dev.ev3 import *
import time

s=ColorSensor('in1')
print(s.reflected_light_intensity)
m=LargeMotor('outA')
n=LargeMotor('outB')

'''



# m.('AB',40,80,'True')
'''
while(1):
    sensorValue = s.reflected_light_intensity
    if sensorValue >= 8 and sensorValue <= 12:
        m.run_timed(time_sp=50, speed_sp=100)
        n.run_timed(time_sp=50, speed_sp=100)
    elif sensorValue < 8:
        m.run_timed(time_sp=50, speed_sp=100)
        n.run_timed(time_sp=50, speed_sp=500)
    else:
        m.run_timed(time_sp=50, speed_sp=500)
        n.run_timed(time_sp=50, speed_sp=100)
    # time.sleep(1)






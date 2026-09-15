import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led=26 #пин с лампой
GPIO.setup(led,GPIO.OUT)
state = 0
period = 1.0
while True:
    GPIO.output(led,state)
    state = (state+1)%2
    time.sleep(period)
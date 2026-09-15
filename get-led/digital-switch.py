import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #режим обращения
led=26 #пин с лампой
GPIO.setup(led,GPIO.OUT) #цифровой выход
button=13
GPIO.setup(button,GPIO.IN) #кнопка - цифровой вход
state = 0
delay = 0.5
while True:
    if GPIO.input(button):
        state = (state+1)%2
        GPIO.output(led,state)
        time.sleep(delay)
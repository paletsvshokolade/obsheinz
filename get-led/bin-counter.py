import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds,GPIO.OUT)
GPIO.output(leds,0)
up = None
down = None
GPIO.setup(up,GPIO.IN)
GPIO.setup(down,GPIO.IN)
num = 0
'''
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
'''
dtb = lambda x: [int(i) for i in bin(x)[2:].zfill(8)] #[2:] чтобы не было приставки 0b
delay = 0.3
while True:
    if GPIO.input(up): # увеличить число
        num += num
        print(num, dtb(num))
        time.sleep(delay)
    if GPIO.input(down): # уменьшить число
        num -= num 
        print(num, dtb(num))
        time.sleep(delay)
    if num<0: num = 0
    if num>255: num = 0
    GPIO.output(leds, dtb(num))

"""
for led, bit in zip(leds, dtb(nums)):
    GPIO.output(led, bit)
"""

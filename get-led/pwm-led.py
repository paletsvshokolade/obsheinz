import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 14 #лампочка
GPIO.setup(led,GPIO.OUT)
pwm = GPIO.PWM(led, 200) #объект управления шим сигналом
duty = 0.0 # коэфициент заполнения
pwm.start(duty) #генерация сигнала на выходе
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0
import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self,dynamic_range,compare_time=0.01,verbose=False):
        self.dynamic_range=dynamic_range
        self.verbose=verbose
        self.comare_time=compare_time

        self.bits_gpio=[26,20,19,16,13,12,25,11]
        self.comp_gpio=21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio,GPIO.OUT,initial=0)
        GPIO.setup(self.comp_gpio,GPIO.IN)
    def deinit(self):
        GPIO.output(self.bits_gpio,0)
        GPIO.cleanup()
    def number_to_dac(self,number): #подает число на ЦАП
        GPIO.output(self.bits_gpio,[int(element) for element in bin(number)[2:].zfill(8)])
    def sequential_counting_adc(self):
        for i in range(0,256):
            self.number_to_dac(i)
            time.sleep(self.comare_time)
            if GPIO.input(self.comp_gpio):
                return i
        return i
    def get_sc_voltage(self):
        return self.sequential_counting_adc()/256 * self.dynamic_range


if __name__=='__main__':
    try:
        dac = R2R_ADC(3.16)
        while True:
            try:
                print(f'Подобранное напряжение: {dac.get_sc_voltage()}')
            except ValueError:
                print('Вы ввели не число, попробуйте еще раз\n')
    finally:
        dac.deinit()
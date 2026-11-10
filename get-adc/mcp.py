import mcp3021_driver
import time
import adc_plot

adc=mcp3021_driver.MCP3021(5.18)

voltages=[]
times=[]
duration=60

if __name__=='__main__':
    try:
        t1=time.time()
        while time.time()-t1<duration:
            voltages.append(adc.get_voltage())
            times.append(time.time()-t1)
            #if voltages[-1]>4.47: print('take up jumper')
        print(voltages[-25:])
        adc_plot.plot_voltage_vs_time(times, voltages, 5.18,True,'full_charge_grid',True)
        #adc_plot.plot_sampling_period_hist(times)
    finally:
        adc.deinit()
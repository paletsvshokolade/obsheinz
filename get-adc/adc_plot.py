import matplotlib.pyplot as plt

def plot_voltage_vs_time(time,voltage,max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.xlabel('time')
    plt.ylabel('voltage')
    plt.ylim(0,max_voltage)
    plt.xlim(0,3)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = [time[i]-time[i-1] for i in range(1,len(time))]
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.ylabel('number of measures')
    plt.xlabel('time of measure')
    plt.grid()
    plt.show()
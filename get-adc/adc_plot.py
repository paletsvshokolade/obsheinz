import matplotlib.pyplot as plt

def plot_voltage_vs_time(time,voltage,max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.xlabel('time')
    plt.ylabel('voltage')
    plt.ylim(0,max_voltage)
    plt.xlim(0,3)
    plt.show()
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil
from collections import deque

cpu_data = deque(maxlen=30)
mem_data = deque(maxlen=30)
x_data = deque(maxlen=30)

def update_graph(i):
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    cpu_data.append(cpu)
    mem_data.append(mem)
    x_data.append(i)

    ax1.clear()
    ax2.clear()

    ax1.plot(x_data, cpu_data, label='CPU Usage (%)', color='cyan')
    ax2.plot(x_data, mem_data, label='Memory Usage (%)', color='magenta')

    ax1.set_ylim(0, 100)
    ax2.set_ylim(0, 100)

    ax1.set_title("Real-Time CPU Usage")
    ax2.set_title("Real-Time Memory Usage")
    ax1.legend()
    ax2.legend()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ani = animation.FuncAnimation(fig, update_graph, interval=1000)

plt.tight_layout()
plt.show()

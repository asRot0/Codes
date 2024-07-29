import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 2, 6, 14, 30, 43, 75]

plt.xlabel('Time', fontsize=12)
plt.ylabel('Speed', fontsize=12)
plt.title('Speed vs Time')

plt.plot(x, y, 'co--')
plt.show()
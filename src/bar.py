import matplotlib.pyplot as plt

plt.bar(data_a['x'], data_a['y'], label='data a', color='red')
plt.bar(data_b['x'], data_b['y'], label='data b', color='blue')

plt.legend()
plt.show()

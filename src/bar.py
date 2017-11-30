import matplotlib.pyplot as plt

data_a= {
    'x': (1, 2, 3),
    'y': (1, 2, 3),
}

data_b= {
    'x': (1, 2, 3),
    'y': (3, 4, 5),
}

plt.bar(data_a['x'], data_a['y'], label='data a', color='red')
plt.bar(data_b['x'], data_b['y'], label='data b', color='blue')

plt.legend()
plt.show()

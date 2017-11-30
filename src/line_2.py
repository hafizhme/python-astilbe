import matplotlib.pyplot as plt

data_a= {
    'x': (1, 2, 3, 4, 5, 6, 7),
    'y': (16, 8, 4, 2, 1, 2, 3),
}

data_b= {
    'x': (1, 2, 3, 4, 5, 6, 7),
    'y': (3, 2, 1, 2, 4, 8, 16),
}

plt.plot(data['x'], data['y'], label='data a', color='red')
plt.plot(data['x'], data['y'], label='data b', color='blue')

plt.show()

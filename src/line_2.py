import matplotlib.pyplot as plt

data_a= {
    'x': (1, 2, 3),
    'y': (1, 2, 3),
}

data_b= {
    'x': (1, 2, 3),
    'y': (3, 4, 5),
}

plt.plot(data['x'], data['y'], label='data a')
plt.plot(data['x'], data['y'], label='data b')

plt.show()

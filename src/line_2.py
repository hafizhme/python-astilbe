import matplotlib.pyplot as plt

points_a= {
    'x': (1, 2, 3),
    'y': (1, 2, 3),
}

points_b= {
    'x': (1, 2, 3),
    'y': (3, 4, 5),
}

plt.plot(points['x'], points['y'], label='line a')
plt.plot(points['x'], points['y'], label='line b')

plt.show()

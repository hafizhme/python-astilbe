import matplotlib.pyplot as plt

plt.pie(
    sizes=(12, 59, 54, 21, 63),
    explode=(0, 0, 0, 0.1, 0),
    labels=('Pisang', 'Susu', 'Keju', 'Cokelat', 'Jagung'),
    shadow=True,
    startangle=32
)

plt.show()

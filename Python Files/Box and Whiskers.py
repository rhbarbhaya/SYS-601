import matplotlib.pyplot as plt

data = [214.22,
356.32,
19.21,
239.29,
43.52,
63.64,
45.14,
117.88]
plt.boxplot(data)
plt.title("Yellow Team Box and Whiskers Plot")
plt.text(60, .025, 'min = 19.21,\nmedian = 90.76, \nmax = 356.32')
plt.show()
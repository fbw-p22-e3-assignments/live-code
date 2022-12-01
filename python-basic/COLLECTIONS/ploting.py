import matplotlib.pyplot as plt

x = [10, 100, 1000, 10000, 100000]
y = [10, 20, 300, 4000, 100000]
y2 = [p**2 for p in x]

plt.plot(x, y, label='Bla')
plt.plot(x, y2, label='x**2')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')


plt.show()
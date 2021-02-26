import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [0, 5, 10, 15]
y = [10, 5, 7, 11]
x1 = [0, 5, 10, 15]
y1 = [20, 15, 10, 5]

plt.plot(x, y)
plt.plot(x1, y1)
plt.title('graph chart')
plt.xlabel('This is my X axis')
plt.ylabel('This is my Y axis')

plt.show()
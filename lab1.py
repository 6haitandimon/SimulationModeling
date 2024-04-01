import numpy as np
import matplotlib.pyplot as plot

A = np.array([[2, 2], [2, 4]])
B = np.array([16, 26])

print("lin solve : ", np.dot(np.linalg.inv(A), B))


def task4(x):
    if type(x) is np.ndarray:
        return np.linalg.matrix_power(x, 3)*(-1/2) - np.linalg.matrix_power(x, 2) * 2 - 2
    else:
        return (-1/2)*x*x*x - 2*x*x - 2


print(task4(3))
print(task4(np.array([[1, 1], [2, 2]])))

x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = []

for item in x:
    y.append(task4(item))

plot.plot(x, y, marker='*')
plot.title("x(y)")
plot.xlabel("x label")
plot.ylabel("y label")
plot.grid()
plot.show()
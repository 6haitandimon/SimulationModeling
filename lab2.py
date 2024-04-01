import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

M = 8000
K = 12
l = 0.5


def PrintK(array):
    for i in range(K):
        print(array[i], end=" ")
    print()


def SetPart(array, k):
    res = []
    for i in range(k):
        res.append(array[i])

    return res


normalDistribution = np.random.randn(M)
normalDistribution32 = SetPart(normalDistribution, 32)
normalDistribution316 = SetPart(normalDistribution, 316)
normalDistribution1000 = SetPart(normalDistribution, 1000)
normalDistribution3162 = SetPart(normalDistribution, 3162)

discreteDistribution = np.random.poisson(l, size=M)
discreteDistribution32 = SetPart(discreteDistribution, 32)
discreteDistribution316 = SetPart(discreteDistribution, 316)
discreteDistribution1000 = SetPart(discreteDistribution, 1000)
discreteDistribution3162 = SetPart(discreteDistribution, 3162)

print("Нормальное распределение:")
PrintK(normalDistribution)
print(min(normalDistribution), " -min")
print(max(normalDistribution), " -max")
print(np.mean(normalDistribution), " -математическое ожидание")
print(np.std(normalDistribution), " -среднеквадратичечкое отклонение")

print("Дискреьное распределение:")
PrintK(discreteDistribution)
print(min(discreteDistribution), " -min")
print(max(discreteDistribution), " -max")
print(np.mean(discreteDistribution), " -математическое ожидание")
print(np.std(discreteDistribution), " -среднеквадратическое отклонение")

normalDistributionMatY = [np.mean(normalDistribution32), np.mean(normalDistribution316), np.mean(normalDistribution1000), np.mean(normalDistribution3162),
                          np.mean(normalDistribution)]
discreteDistributionMatY = [np.mean(discreteDistribution32), np.mean(discreteDistribution316), np.mean(discreteDistribution1000), np.mean(discreteDistribution3162),
                            np.mean(discreteDistribution)]

MatX = [math.log10(32), math.log10(316), math.log10(1000),
        math.log10(3162), math.log10(M)]

plt.plot(MatX, normalDistributionMatY, marker='*')
plt.plot(MatX, discreteDistributionMatY, marker='*')
plt.title("Математическое ожидание")
plt.grid()
plt.show()

plt.hist(normalDistribution, density=True, bins=100)
x = np.linspace(-4, 4, M)
plt.plot(x, norm.pdf(x, 0, 1), 'r')
plt.title("Нормальное распределение")
plt.show()

plt.hist(discreteDistribution, density=True, bins=100)
plt.title("Дискретное распределение")
plt.show()

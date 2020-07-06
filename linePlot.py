import numpy.random as rand
import numpy as np
import matplotlib.pyplot as plt


def dataGenerate(fun, size):
    x = np.arange(size)
    y = fun(x) + 3*rand.standard_normal(size)
    return x, y


def plot(funArray, size):

    # generate data points
    x, dataPoints = dataGenerate(funArray[0], size)

    # set figure
    colorMap = ['lightcoral', 'salmon', 'coral',
                'sandybrown', 'y', 'limegreen', 'lightseagreen']
    plt.figure(figsize=(12, 8))
    plt.scatter(x, dataPoints, color=colorMap[0], label="Data points")
    for ii in range(len(funArray)):
        plt.plot(x, funArray[ii](x), color=colorMap[(ii+1) %
                                                    len(colorMap)], label="Function #%d" % ii)
    plt.legend()
    plt.xlabel(r'$x$', fontsize=12)
    plt.show()


def fun1(x):
    return 2*x


def fun2(x):
    return -x + 2


def fun3(x):
    return 5*x - 3


def fun4(x):
    return x


if __name__ == '__main__':
    plot([fun1, fun2, fun3, fun4], 10)

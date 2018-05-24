import unittest
import junit.myDes


class TestMatplotlib(unittest.TestCase):
    def test01(self):
        import numpy as np
        import matplotlib.pyplot as plt

        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)

        # 数据的直方图
        n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        plt.title('Histogram of IQ')
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.axis([40, 160, 0, 0.03])
        plt.grid(True)
        plt.show()

    def test02(self):
        import matplotlib.pyplot as plt

        x = [0] * 65
        for i in range(0, 100):
            x[junit.myDes.inputChange(1)] += 1

        print(x)
        # 数据的直方图
        import numpy
        index = numpy.arange(65)
        print(index)
        plt.bar(index, x)

        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        plt.title('Histogram of IQ')
        # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        # plt.axis([1, 64, 0, 50])
        plt.grid(True)
        plt.savefig("pic.png")

    def testFigure(self):
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_agg import FigureCanvasAgg

        fig = Figure(figsize=[6, 6])

        ax = fig.add_axes([.1, .1, .8, .8])
        ax.scatter([0.2, 0.3], [0.25, 0.35])
        fig.show("ss")
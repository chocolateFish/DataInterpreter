# Chart View
class ChartView:

    def draw_plot(self, title, xlabel, ylabel, xdata, ydata):
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        plt.plot(xdata, ydata)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()
        plt.show()
        # plt.savefig('myfig')


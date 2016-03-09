# Chart View - doesn't need to be a class yet, but leaving as is for structure


class ChartView:
    def __intit__(self):
        self.__my_controller = None

    def set_controller(self, the_controller):
        self.__my_controller = the_controller

    def draw_plot(self, title, xlabel, ylabel, xdata, ydata):
        try:
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            plt.plot(xdata, ydata, label="")
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.title(title)
            plt.show()
            #plt.savefig('myfig')
        except Exception as e:
            raise e
        else:
             # actually - pass to the controller to save
             plt.savefig('myfig')






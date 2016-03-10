# Chart View - doesn't need to be a class yet, but leaving as is for structure


class ChartView:
    def __intit__(self):
        self.__my_controller = None
        self.title = "Data Chart"

    def set_controller(self, the_controller):
        self.__my_controller = the_controller

    # refactor
    def draw_plot(self,x_label, y_label, x_data, y_data):
        try:
            x_data.sort()
            y_data.sort()
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            plt.plot(x_data, y_data, label="")
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            title = '{0} {1} RELATIONSHIP'.format(x_label, y_label)
            plt.title(title)
            plt.show()
            #plt.savefig('myfig')
        except Exception as e:
            raise e
        else:
             # actually - pass to the controller to save
             plt.savefig('myfig')

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
def drawGraph(objects,performance,title):
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel("Number")
    plt.title(title)

    plt.show()
    plt.savefig('bargraph.png')

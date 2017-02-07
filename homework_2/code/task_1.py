from task_2 import abs_lagrange_operator
import numpy as np
from matplotlib import pyplot as plt


def main():
    plt.figure(2)
    subplt = 221
    legend = []
    abs_max = []
    X = np.linspace(-1, 1, 1000, endpoint=True)
    Xp = np.linspace(0.8, 1, 100)
    n = 2
    for x in Xp:
        points = [-x, 0, x]
        abs_L = abs_lagrange_operator(points, X)
        abs_max.append(max(abs_L))
        #pos_num = get_position(max(abs_L), abs_L)
        print(str(x) + " & " + str(max(abs_L)) + " \\\\") 
        #plt.subplot(subplt)
        #
        #legend.append(str(x))
        #subplt = subplt + 1
    #plt.plot(X, abs_max)
    # plt.legend(legend)
    #plt.savefig("task_1.png")

if __name__ == "__main__":
    main()
    

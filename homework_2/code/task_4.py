from task_2 import abs_lagrange_operator
import numpy as np
from matplotlib import pyplot as plt

def get_position(myelement, mylist):
    for i in range(len(mylist)):
        if mylist[i] == myelement:
            return i
    return "no such element"

if __name__ == "__main__":
    X = np.linspace(-1, 1, 1000, endpoint=True)
    # plt.figure(1)
    # subplt = 221
    # for n in [3.0, 5.0, 7.0, 9.0]:
    #     points_equal = []
    #     points_cheby = []
    #     for i in range(int(n+1)):
    #         points_equal.append(2*i/float(n)-1) # Equally spaced
    #         points_cheby.append(np.cos( (2*(n-i) + 1) / (2*(n+1)) * np.pi ) )
    #     norm_equal = abs_lagrange_operator(points_equal, X)
    #     norm_cheby = abs_lagrange_operator(points_cheby, X)
    #     pos_num = get_position(max(norm_cheby), norm_cheby)
    #     print(str(n) + " : " + str(X[pos_num]) + " : " + str(max(norm_cheby)))
    #     plt.subplot(subplt)
    #     plt.plot(X, norm_cheby)
    #     plt.legend(str(n))
    #     subplt = subplt + 1
    # plt.savefig("task_4_cheby.png")

    plt.figure(2)
    subplt = 221
    legend = []
    abs_max = []
    Xp = np.linspace(0.8, 1, 100, endpoint=False)
    n = 2
    for x in Xp:
        points = [-x, 0, x]
        abs_L = abs_lagrange_operator(points, X)
        abs_max.append(max(abs_L))
        #pos_num = get_position(max(abs_L), abs_L)
        print(str(x) + " : " + str(max(abs_L)))
        #plt.subplot(subplt)
        #
        #legend.append(str(x))
        #subplt = subplt + 1
    plt.plot(X, abs_max)
    # plt.legend(legend)
    plt.savefig("task_1.png")

    # plt.figure(3)
    # subplt = 311
    # legend = []
    # for x in [0.4, 0.5, 0.6]:
    #     points = [-1, -x, x, 1]
    #     abs_L = abs_lagrange_operator(points, X)
    #     pos_num = get_position(max(abs_L), abs_L)
    #     #plt.subplot(subplt)
    #     plt.plot(X, abs_L)
    #     legend.append(str(x))
    #     subplt = subplt + 1

    # plt.legend(legend)
    # plt.savefig("task_4_n3.png")

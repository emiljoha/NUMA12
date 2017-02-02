# Calculate lebesge constants using brute force method

from task_3 import lagrange
import numpy as np
from matplotlib import pyplot as plt

def abs_lagrange_operator(points, X):
    """ intervall = (a, b), points = [x_0,...,x_n]
    X = points of evaluation.
    """
    res = [0]*len(X); 
    for k in range(len(points)):
        lagrange_values = lagrange(k, points, X)
        for i in range(len(X)):
            res[i] += np.abs(lagrange_values[i])
    return res

if __name__ == "__main__":
    X = np.linspace(-1, 1, 1000, endpoint=True)
    print("\\begin{tabular}{ l | c | r }")
    print("number of points & Equal & Chebychef \\\\ \\hline")
    for n  in [2.0, 4.0, 6.0, 8.0, 10.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0]:
        points_equal = []
        points_cheby = []
        for i in range(int(n+1)):
            points_equal.append(2*i/float(n)-1) # Equally spaced
            points_cheby.append(np.cos( (2*(n-i) + 1) / (2*(n+1)) * np.pi ) )
        norm_equal = abs_lagrange_operator(points_equal, X)
        norm_cheby = abs_lagrange_operator(points_cheby, X)
        print(str(int(n+1)) + " & " + str(max(norm_equal)) + " & " + str(max(norm_cheby)) + " \\\\" )
    # plt.plot(X, abs_L)
    # #plt.legend(["$l_0$", "$l_1$", "$l_2$"])
    # plt.savefig("task_2.png")
    print("\end{tabular}")

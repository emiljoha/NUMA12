## Task 1: The exchange algorithm

from sympy import symbols, lambdify, sin
import numpy as np
from matplotlib import pyplot as plt

def sign(x):
    if x <= 0:
        return -1
    if x > 0:
        return 1
     
def hcoeff(x):
    try:
        res = [];
        for k in x:
            res.append((-1)**k);
        return res;
    except TypeError:
        return (-1)**k;


def polynom(x, basis, coef):
    try:
        res = np.zeros(len(x));
        for i in range(len(coef)):
            for j in range(len(x)): 
                res[j] += coef[i] * basis(x[j], i);
        return res;
    except TypeError: # x not list but number.
        res = 0;
        for i in range(len(coef)):
                res[j] += coef[i] * basis(x, i);
        return res;

def error(f, x, basis, coef):
    return f(x) - polynom(x, basis, coef);


def exchange_algorithm (f, n, intervall, reference, tolerance, nsp, basis=pow):
    if (len(reference) != n + 1):
        raise ValueError("Reference must have exactly n+1 elements")
    
    a, b = intervall
    
    matrix = np.zeros([n+1, n+1])
    grid = np.linspace(a, b, num=nsp)
    h = [];
    count = 0;

    legend = []; # for plotting
    
    while ( (len(h) < 2
             or (abs(h[len(h)-1] - h[len(h) - 2]) > tolerance))
            and count < 10):
        count += 1
        # Set up matrix from reference 
        for i in range(n):
            for j in range(n+1):
                matrix[i][j]= basis(reference[j], i)
        matrix[n] = hcoeff(np.array(range(n+1)))
        
        #calculate coefficients and h
        #res =  np.linalg.inv(np.transpose(matrix)).dot(f(reference))
        res = np.linalg.solve(np.transpose(matrix), f(reference))
        h.append(res[n])
        
        # Find the max
        coefficients = np.delete(res, -1);
        error_grid = error(f, grid, basis, coefficients);
        error_ref = error(f, reference, basis, coefficients);
        max_index = np.argmax(np.abs(error_grid)); 
        maxpos = grid[max_index]; 
        max_error = error_grid[max_index];
        plt.plot(grid, error_grid);
        #plt.plot(reference, np.zeros(len(reference)), "*")
        legend.append(str(count))

        #Case: Before first
        if (maxpos < reference[0]):
            if (sign(max_error) == sign(error_ref[0])):
                reference[0] = maxpos
            else:
                reference = np.delete(reference, n)#delete last element
                reference = np.insert(reference, 0, maxpos) #insert maxpos as first
        
        #Case: between two reference points
        for i in range(len(reference)-1):
            if ( (maxpos > reference[i]) and (maxpos < reference[i+1]) ):
                if (sign(max_error) == sign(error_ref[i])):
                    reference[i] = maxpos
                else:
                    reference[i+1] = maxpos
 
        #Case: After last point
        if (maxpos > reference[n]):
            if (sign(max_error) == sign(error_ref[n])):
                reference[n] = maxpos
            else:
                reference = np.delete(reference, 0) #delete first element.
                reference = np.append(reference, maxpos) # append with new last element.
    plt.legend(legend)
    plt.savefig("error.png")
    plt.figure(2);
    plt.plot(grid, f(grid), grid, polynom(grid, basis, coefficients))
    plt.legend(["f", "approx"])
    plt.savefig("approx.png")
    return coefficients, np.abs(max_error), count, h, reference; 
    
if __name__ == "__main__":
    def f(x):
        try:
            return 1 / (1 + 25*x**2);
        except TypeError:
            res = [];
            for y in x:
                res.append(1 / (1 + 25*x**2));
            return res; 
    
    x = symbols('x')
    n = 40
    intervall = (0, 1)
    reference = np.linspace(0, 1, n+1)
    tolerance = 10**(-10)
    nsp = 100
    coef, error, count, h, reference = exchange_algorithm(f, n, intervall, reference, tolerance, nsp)
    print("Coefficients: " + str(coef))
    print("error: " + str(error))
    print("count: " + str(count))
    print("h: " + str(h))
    print("reference: " + str(reference))
    

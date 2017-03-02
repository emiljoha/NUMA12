import sympy as sp
import scipy.special
import math
import numpy

    
def gauss(intervall, f, k):
    a, b = intervall;
    x = sp.symbols('x');
    
    #Legendre polynomial
    Lk = 0;
    for i in range(k+1):
        Lk += scipy.special.binom(k, i)**2 * (x - 1)**(k - i) * (x + 1)**i;
    Lk *= 2**(-k);

    #We need to find the coefficients to use numpy.roots 
    coefficients = []
    for i in range(k):
        coefficients.append(sp.expand(Lk).coeff(x**(k-i)))
    coefficients.append(sp.expand(Lk).subs(x, 0).evalf())
    print(coefficients);
    
    roots = numpy.roots(coefficients);
    
    # lagrange polynomials
    def lagrange(points):
        l = [];
        for i in range(len(points)):
            li = 1
            for j in range(len(points)):
                if (i != j):
                    li *= (x - points[j]) / (points[i] - points[j])
                    li = sp.simplify(li)
            l.append(li)
        return l

    lagpols = lagrange(roots);
    
    #Integrating the lagrange polynomials to find the weighs 
    weights = [];
    for lag in lagpols:
        weights.append(sp.integrate(lag, (x, -1, 1)).evalf());

    res = 0;
    for i in range(k):
        res += weights[i] * f((b - a) * roots[i] / 2 + (a + b) / 2)
    return (b - a ) / 2 * res;  

def func(val):
    #Definition of the function to integrate
    return 0.764 * math.sqrt(math.log(val))**(-1);  
    
if (__name__ == "__main__"):
    print(gauss([1, 30], func, 15));
    x = sp.symbols('x');
    #integrate with sympy to compare results
    print(sp.integrate(0.764 / sp.sqrt(sp.log(x)), (x, 1, 30)).evalf())
    

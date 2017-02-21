import numpy as np
from matplotlib import pyplot as plt
from sympy import *

x = symbols('x')
pexpr = x - Rational(1,8)
fexpr = x**2
errorexpr = pexpr - fexpr

p = lambdify(x, pexpr, "numpy")
f = lambdify(x, fexpr, "numpy")
error = lambdify(x, errorexpr, "numpy")

Grid = np.linspace(0, 1, 1000)
maxerrorup = []
maxerrordown = []
for i in range(len(Grid)):
    maxerrorup.append(1/8)
    maxerrordown.append(-1/8)
    
plt.figure(1)
plt.plot(Grid, p(Grid), Grid, f(Grid));
plt.legend(["$x - 1/8$", "$x^2$"])
plt.savefig("task_2_approximation.png")

plt.figure(2)
plt.plot(Grid, error(Grid), Grid, maxerrorup, Grid, maxerrordown)
plt.legend(["Error", "1/8", "-1/8"])
plt.savefig("task_2_error.png")

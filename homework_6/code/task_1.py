import sys
import sympy as sp

x, a, b, c = sp.symbols('x a b c')

# Choose Q2 to be monic
Q2 = a + b*x + x**2

# scalar product
def scalar(func1, func2):
    #print(sp.latex(sp.integrate(x*func1*func2, (x, 0, 1))))
    return sp.integrate(x*func1*func2, (x, 0, 1))

# Need to make Q2 such that it is orthogonal to all elements in
# P_1.
sol = sp.solve([scalar(Q2, 1), scalar(Q2, x)]) 
Q2 = Q2.subs([(a, sol[a]), (b, sol[b])])
#print(sp.latex(sol[a]) + "     " + sp.latex(sol[b]))
# Roots to Q2 will now be out X_i´s 
x0, x1 = sp.solve(Q2, x)

# lagrangian polynomials
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

l0, l1 = lagrange([x0, x1])

#Calculate coeff.
w0 = sp.simplify(scalar(l0, 1))
w1 = sp.simplify(scalar(l1, 1));  

# print('x_0 = ' + sp.latex(x0))
# print('x_1 = ' + sp.latex(x1))
# print('w_0 = ' + sp.latex(w0))
# print('w_1 = ' + sp.latex(w1))


#sys.stdout.write

f = a + b*x + c*x**2
approx = w0*f.subs(x, x0) + w1*f.subs(x, x1)
print(sp.latex(approx))
#print(sp.integrate(x*f, (x, 0, 1)))
print(sp.simplify(approx - sp.integrate(x*f, (x, 0, 1))) == 0)


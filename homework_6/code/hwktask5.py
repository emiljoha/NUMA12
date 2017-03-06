import numpy as np
from matplotlib import pyplot as plt

# data definition
X = [0, 1, 2, 3, 4, 5, 6];
f = [-35, -56, 0, -16, -3, 4, 10];
w = np.ones(7)
#sets Z and complements of Z
Z = [];

# Construction of all possible Z.
for i in range(len(X)):
    for j in range(i+1, len(X)):
            Z.append([i, j]);
            
all_errors = [];
all_approx = []
for k in range(len(Z)):
    i, j = Z[k];
    #construct approximation
    p = [(f[j] * X[i] - f[i] * X[j]) /  (X[i] - X[j]), 
         (f[i] - f[j]) / float(X[i] - X[j])]
    
    # Calculate error
    error = 0;
    for l in range(len(X)):
        error += w[l] * np.abs(f[l] - (p[1] * X[l] + p[0]) );

    all_errors.append(error);
    all_approx.append(p);

best_approx_index = np.argmin(np.array(all_errors))
p_star = all_approx[best_approx_index]
approx = []
for x in X:
    approx.append(p_star[1] * x + p_star[0])

print("data: " + str(f))
print("approx: " + str(approx))
print("polynom: " + str(p_star[1]) + "*x + "
      + str(p_star[0]))

approx = []p
grid = np.linspace(X[0], X[-1], 100)
for x in grid:
    approx.append(p_star[1] * x + p_star[0])

plt.plot(approx, grid);
plt.plot(f, X, "*");
plt.legend(["$p^*(x)$ = " + str(p_star[1]) + "x " + str(p_star[0]), "data points"]) 
plt.savefig("task_5.png")


## Task 1: The exchange algorithm

from sympy import symbols, lambdify, sin
import numpy as np

def sign(x):
    if x <= 0:
        return -1
    if x > 0:
        return 1

# @param f Continuos function to be approximated
# @param n Dimension of appriximation space
# @param intervall [a, b] end points of closed intervall on whitch the
#                  function f is to be approximated.
# @param refrence Ordered list of n+1 distingt point in [a, b]
# @param tolerance When h changes less that tolerance the algorithm ends.
# @param nsp Number of sample points when calculating maxima of error function.
# @param basis Optional set of n Sympy expression that form the functional
#              basis for the approximation set. If not provided the approximation
#              set of polynomials of degree n-1 with the monomial basis is used.

# @return Coefficients Array of coefficients for the found approximation in the basis.
# @return Error Estimate of the error (distance to the best approximation
#               in the max-norm
# @return h_history Vector with the reference level values h for every iteration.
# @return final_reference The current reference when done. 
def exchange_algorithm (f_symb, n, intervall, reference, tolerance, nsp, basis_symb=" " ):
    if basis_symb == " ":
        basis_symb = []
        x = symbols('x')
        for i in range(n):
            basis_symb.append(x**i)

    a, b = intervall
    print(reference)

    #translate from sympy numpy functions
    f = lambdify(x, f_symb, "numpy")

    basis = []
    for i in range(n):
        basis.append(lambdify(x, basis_symb[i], "numpy"))
        
    hcoeff = lambdify(x, (-1)**x, "numpy")
        
    matrix = np.zeros([n+1, n+1])
    grid = np.linspace(a, b, num=nsp)
    h = [];
    count = 0; 

    while ( (len(h) < 2 or (abs(h[len(h)-1] - h[len(h) - 2]) > tolerance)) and count < 100):
        count += 1
        # Set up matrix from reference 
        for i in range(n):
            matrix[i] = basis[i](reference)
        matrix[n] = hcoeff(np.array(range(n+1)))

        #calculate coefficients and h
        #res =  np.linalg.inv(np.transpose(matrix)).dot(f(reference))
        res = np.linalg.solve(matrix, f(reference))
        h.append(res[n])

        # Symbolic represenation of approximation
        approx_symb = 0
        for i in range(n):
           approx_symb += res[i] * basis_symb[i]

        # Construct symbolic representaion of error function
        error_symb = f_symb - approx_symb
        error = lambdify(x, error_symb, "numpy")

        # Find the max 
        error_array = error(grid)
        abs_max_error = max(np.absolute(error_array))
        for i in range(n):
            if (np.abs(error_array[i]) == abs_max_error) :
                index = i
                break
        maxpos = grid[index]
        print(maxpos)

        #Exchange point in reference.
        max_error = error(maxpos)

        # Test if we are done. 
        for i in range(n):
            if (maxpos == reference[i]):
                return res, h, maxpos;

        #Case: Before first
        if (maxpos < reference[0]):
            if (sign(max_error) == sign(error(reference[0])) ):
                reference[0] = maxpos
            else:
                reference = np.delete(reference, n)#delete last element
                reference = np.insert(reference, 0, maxpos) #insert maxpos as first
        #Case: between two reference points
        for i in range(len(reference)-2):
            if ( (maxpos > reference[i]) and (maxpos < reference[i+1]) ):
                if (sign(max_error) == sign(error(reference[i]))):
                    reference[i] = maxpos
                else:
                    reference[i+1] = maxpos                
        #Case: After last point
        if (maxpos > reference[n]):
            if (sign(max_error) == sign(error(reference[n]))):
                reference[n] = maxpos
            else:
                reference = np.delete(reference, 0) #delete first element.
                reference = np.append(reference, maxpos) # append with new last element.
        print(reference)
    return res, h, maxpos

    
if __name__ == "__main__":
    x = symbols('x')
    n = 2
    intervall = (0, 1)
    reference = np.array([0, 0.3, 1])
    f = x**2 #1 / ( 1 + 25*x**2)
    tolerance = 0.01
    nsp = 1000
    res, h, maxpos= exchange_algorithm(f, n, intervall, reference, tolerance, nsp)
    print(res)

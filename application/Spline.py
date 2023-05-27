import numpy as np
from scipy import linalg

class Spline():
    def splineLineal(x, y):
        output = {
            "errors": list()
        }
        x = np.array(x)
        y = np.array(y)
        n = x.size
        m = 2*(n-1) #factor m para la formula de los trazadores
        A = np.zeros((m, m))
        b = np.zeros((m, 1))
        Coef = np.zeros((n-1, 2))
        i = 0
        # Interpolating condition
        try:
            while i < x.size-1:
                A[i+1, [2*i+1-1, 2*i+1]] = [x[i+1], 1]  #Realiza la formula de interpolacion de superficie 
                b[i+1] = y[i+1]
                i = i+1

            A[0, [0, 1]] = [x[0], 1]
            b[0] = y[0]
            i = 1
            # Condition of continuity
            while i < x.size-1:
                A[x.size-1+i, 2*i-2:2*i+2] = np.hstack((x[i], 1, -x[i], -1))
                b[x.size-1+i] = 0
                i = i+1
            Saux = linalg.solve(A, b)
            # Order Coefficients
            i = 0
            while i < x.size-1:
                Coef[i, :] = [Saux[2*i], Saux[2*i+1]]
                i = i+1

        except BaseException as e:
            output["errors"].append("Error in data: " + str(e))
            return output

        output["results"] = Coef
        return output
        

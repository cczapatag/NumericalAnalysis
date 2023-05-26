from numpy.linalg import inv, eigvals, norm

import numpy as np

class Jacobi():
    def jacobi(a,b,x0,n,tol):
        tableListData = []
        tempMapIterData = {}

        l = -np.tril(a, -1)
        u = -np.triu(a, 1)
        d = a + l + u
        t = np.matmul(inv(d), l + u)
        c = np.matmul(inv(d), b)
        if max(abs(eigvals(t))) > 1:
            return tableListData, "The function doesn't converge"
        
        if np.linalg.det(a) == 0:
            return tableListData, "det(A) is 0. The method cannot be executed."


        xn = np.matmul(t, x0) + c
        cont = 0
        e = 1000
        while (x0 != xn).all() and cont < n and e > tol:
            x0 = xn
            xn = np.matmul(t, x0) + c
            cont += 1
            e = norm(x0 - xn)
            tempMapIterData['iteracion'] = str(cont)
            tempMapIterData['x0'] = str(x0)
            tempMapIterData['xn'] = str(xn)
            tempMapIterData['E'] = '{:.1e}'.format(e).replace('e-0', 'e-')
            tableListData.append(tempMapIterData.copy())
            tempMapIterData.clear()
        return tableListData, f'It converge at the point = {str(xn)}'
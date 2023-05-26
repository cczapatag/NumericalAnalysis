import numpy as np

class SOR():
    def sor(a, b, x0, w, tol, n):
        
        a = np.array(a)
        b = np.array(b)

        tableListData = []
        tempMapIterData = {}
        cont = 0
        phi = x0[:]
        residual = np.linalg.norm(np.matmul(a, phi) - b)
        while residual > tol and cont < n:
            for i in range(a.shape[0]):
                sigma = 0
                for j in range(a.shape[1]):
                    if j != i:
                        sigma += a[i, j] * phi[j]
                phi[i] = (1 - w) * phi[i] + (w / a[i, i]) * (b[i] - sigma)
            residual = np.linalg.norm(np.matmul(a, phi) - b)
            cont += 1
            print("cont {} Residual: {:10.6g}".format(cont, residual))
            tempMapIterData['Iteracion'] = str(cont)
            tempMapIterData['Resultado'] = str(residual)
            tempMapIterData['xn'] = str(phi)
            tableListData.append(tempMapIterData.copy())
            tempMapIterData.clear()



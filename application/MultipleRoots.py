from math import *

class MultipleRoots():
    def multiple_roots(f, df, df2, x0, tol, max_iterations):
        """
        Encuentra una raíz de la función f(x) utilizando el método de las raíces múltiples.

        Args:
        f: Función que se evalúa.
        df: Primera derivada de la función f(x).
        df2: Segunda derivada de la función f(x).
        x0: Valor inicial para comenzar la iteración.
        tol: Tolerancia para el error absoluto entre las aproximaciones sucesivas. Debe ser un número positivo.
        max_iterations: Número máximo de iteraciones permitidas. Debe ser un entero positivo.

        Returns:
        Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
        donde cada lista contiene el número de iteración, el valor de x en la iteración actual, el valor de f(x) en la
        iteración actual y el error absoluto entre las aproximaciones sucesivas. El segundo elemento es un mensaje
        indicando si se encontró una raíz o si se alcanzó el número máximo de iteraciones.
        """
        
        results = []
        
        valorX = {'x': x0}
        
        fx = eval(f, globals(), valorX)
        dfx = eval(df, globals(), valorX)
        df2x = eval(df2, globals(), valorX)
        
        iteration = 0
        error = tol + 1
        results.append([iteration, x0, fx, float('nan')])
        
        while fx != 0 and dfx != 0 and error > tol and iteration < max_iterations:
            numerator = fx * dfx
            denominator = dfx**2 - fx * df2x
            x1 = x0 - numerator / denominator
            
            valorX['x'] = x1
            
            fx = eval(f, globals(), valorX)
            dfx = eval(df, globals(), valorX)
            df2x = eval(df2, globals(), valorX)
            
            error = abs(x1 - x0)
            iteration += 1
            results.append([iteration, x1, fx, error])
            
            x0 = x1

        if fx == 0:
            return results, f"{x0} is a root"
        elif error <= tol:
            return results, f"{x0} is an approximation to a root with a tolerance of {tol}"
        else:
            return results, "The maximum number of iterations was reached"

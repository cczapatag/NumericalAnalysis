import pandas as pd
import numpy as np
def fixed_point(f, g, x0, tol, max_iterations):
    """
    Encuentra una raíz de la función f(x) utilizando el método del punto fijo.

    Args:
        f: Función que se evalúa.
        g: Función de iteración.
        x0: Valor inicial para comenzar la iteración.
        tol: Tolerancia para el error absoluto entre las aproximaciones sucesivas. Debe ser un número positivo.
        max_iterations: Número máximo de iteraciones permitidas. Debe ser un entero positivo.

    Returns:
        Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
        donde cada lista contiene el número de iteración, el valor de x en la iteración actual, el valor de f(x) en la
        iteración actual, el valor de g(x) en la iteración actual y el error absoluto entre las aproximaciones
        sucesivas. El segundo elemento es un mensaje indicando si se encontró una raíz o si se alcanzó el número
        máximo de iteraciones.
    """
    if not callable(f):
        raise TypeError("El argumento 'f' debe ser una función.")
    if not callable(g):
        raise TypeError("El argumento 'g' debe ser una función.")
    if not isinstance(x0, (int, float)):
        raise TypeError("El argumento 'x0' debe ser un número.")
    if not isinstance(tol, (int, float)) or tol <= 0:
        raise ValueError("El argumento 'tol' debe ser un número positivo.")
    if not isinstance(max_iterations, int) or max_iterations <= 0:
        raise ValueError(
            "El argumento 'max_iterations' debe ser un entero positivo.")

    results = []
    x = x0
    fx = f(x)
    iteration = 0
    error = tol + 1
    results.append([iteration, x, fx, g(x), float('nan')])
    while fx != 0 and error > tol and iteration < max_iterations:
        x = g(x)
        fx = f(x)
        error = abs(results[-1][1] - x)
        iteration += 1
        results.append([iteration, x, fx, g(x), error])
    if fx == 0:
        return results, f"{x} es raíz"
    elif error <= tol:
        return results, f"{x} se aproxima a una raíz con una tolerancia de {tol}"
    else:
        return results, "Se alcanzó el número máximo de iteraciones"
    
# Ejemplo de uso
def f(x):
    return -7*np.log(x)+x-2

def g(x):
    return (x-7) / (x)

results, message = fixed_point(f, g, 1, 0.01, 100)
df = pd.DataFrame(results, columns=['Iteración', 'x', 'f(x)', 'g(x)', 'error'])
print(df)
print(message)
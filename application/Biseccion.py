import pandas as pd
from math import *

def bisection(f, a, b, tol, max_iterations):
    """
    Encuentra una raíz de la función f(x) en el intervalo [a, b] utilizando el método de bisección.

    Args:
        f: Función que se evalúa.
        a: Límite inferior del intervalo [a, b].
        b: Límite superior del intervalo [a, b].
        tol: Tolerancia para el error absoluto entre las aproximaciones sucesivas. Debe ser un número positivo.
        max_iterations: Número máximo de iteraciones permitidas. Debe ser un entero positivo.

    Returns:
        Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
        donde cada lista contiene el número de iteración, el límite inferior del intervalo, el valor medio del
        intervalo, el límite superior del intervalo, el valor de f(x) en el valor medio y el error absoluto entre las
        aproximaciones sucesivas. El segundo elemento es un mensaje indicando si se encontró una raíz o si se alcanzó
        el número máximo de iteraciones.
    """
    if not callable(f):
        raise TypeError("El argumento 'f' debe ser una función.")
    if not isinstance(a, (int, float)):
        raise TypeError("El argumento 'a' debe ser un número.")
    if not isinstance(b, (int, float)):
        raise TypeError("El argumento 'b' debe ser un número.")
    if not isinstance(tol, (int, float)) or tol <= 0:
        raise ValueError("El argumento 'tol' debe ser un número positivo.")
    if not isinstance(max_iterations, int) or max_iterations <= 0:
        raise ValueError(
            "El argumento 'max_iterations' debe ser un entero positivo.")

    results = []
    fa = f(a)
    fb = f(b)
    if fa == 0:
        return [], f"{a} es raíz"
    elif fb == 0:
        return [], f"{b} es raíz"
    elif fa * fb < 0:
        x = (a + b) / 2
        fx = f(x)
        iteration = 1
        error = tol + 1
        results.append([iteration, a, x, b, fx, float('nan')])
        while fx != 0 and error > tol and iteration < max_iterations:
            if fa * fx < 0:
                b = x
                fb = fx
            else:
                a = x
                fa = fx
            x_prev = x
            x = (a + b) / 2
            fx = f(x)
            error = abs(x - x_prev)
            iteration += 1
            results.append([iteration, a, x, b, fx, error])
        if fx == 0:
            return results, f"{x} es raíz"
        elif error <= tol:
            return results, f"{x} se aproxima a una raíz con una tolerancia de {tol}"
        else:
            return results, "Se alcanzó el número máximo de iteraciones"
    else:
        return [], "El intervalo es inadecuado"
# Ejemplo de uso
def f(x):
    return log(sin(x)**2+1)-(1/2)

results, message = bisection(f, 0, 1, 1e-7, 100)
df = pd.DataFrame(results, columns=['Iteración', 'x_lower', 'x', 'x_upper', 'f(x)', 'error'])
print(df)
print(message)
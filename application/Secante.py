import pandas as pd

def secante(f, x0, x1, tol, max_iterations):
    """
    Encuentra una raíz de la función f(x) utilizando el método de la secante.

    Args:
        f: Función que se evalúa.
        x0: Primer valor inicial para comenzar la iteración.
        x1: Segundo valor inicial para comenzar la iteración.
        tol: Tolerancia para el error absoluto entre las aproximaciones sucesivas. Debe ser un número positivo.
        max_iterations: Número máximo de iteraciones permitidas. Debe ser un entero positivo.

    Returns:
        Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
        donde cada lista contiene el número de iteración, el valor de x en la iteración actual, el valor de f(x) en la
        iteración actual y el error absoluto entre las aproximaciones sucesivas. El segundo elemento es un mensaje
        indicando si se encontró una raíz o si se alcanzó el número máximo de iteraciones.
    """
    if not callable(f):
        raise TypeError("El argumento 'f' debe ser una función.")
    if not isinstance(x0, (int, float)):
        raise TypeError("El argumento 'x0' debe ser un número.")
    if not isinstance(x1, (int, float)):
        raise TypeError("El argumento 'x1' debe ser un número.")
    if not isinstance(tol, (int, float)) or tol <= 0:
        raise ValueError("El argumento 'tol' debe ser un número positivo.")
    if not isinstance(max_iterations, int) or max_iterations <= 0:
        raise ValueError(
            "El argumento 'max_iterations' debe ser un entero positivo.")

    results = []
    fx0 = f(x0)
    fx1 = f(x1)
    iteration = 0
    error = tol + 1
    results.append([iteration, x0, fx0, float('nan')])
    iteration += 1
    results.append([iteration, x1, fx1, abs(x1 - x0)])
    
    while fx1 != 0 and error > tol and iteration < max_iterations:
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fx2 = f(x2)
        error = abs(x2 - x1)
        iteration += 1
        results.append([iteration, x2, fx2, error])
        
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = fx2

    if fx1 == 0:
        return results, f"{x1} es raíz"
    elif error <= tol:
        return results, f"{x1} se aproxima a una raíz con una tolerancia de {tol}"
    else:
        return results, "Se alcanzó el número máximo de iteraciones"
#Ejemplo de uso
def f(x):
    return x**2 - 4

results, message = secante(f, 0, 3, 0.01, 100)
df = pd.DataFrame(results, columns=['Iteración', 'x', 'f(x)', 'error'])
print(df)
print(message)
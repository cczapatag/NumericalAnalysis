import pandas as pd

def newton_raphson(f, df, x0, tol, max_iterations):
    """
    Encuentra una raíz de la función f(x) utilizando el método de Newton-Raphson.

    Args:
        f: Función que se evalúa.
        df: Derivada de la función f(x).
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
    x = x0
    fx = f(x)
    dfx = df(x)
    iteration = 0
    error = tol + 1
    results.append([iteration, x, fx, float('nan')])
    while fx != 0 and dfx != 0 and error > tol and iteration < max_iterations:
        x -= fx / dfx
        fx = f(x)
        dfx = df(x)
        error = abs(results[-1][1] - x)
        iteration += 1
        results.append([iteration, x, fx, error])
    if fx == 0:
        return results, f"{x} es raíz"
    elif error <= tol:
        return results, f"{x} se aproxima a una raíz con una tolerancia de {tol}"
    else:
        return results, "Se alcanzó el número máximo de iteraciones"
    
#Ejemplo de uso
def f(x):
    return x**2 - 4

def df(x):
    return 2*x

results, message = newton_raphson(f, df, 1, 0.01, 100)
df = pd.DataFrame(results, columns=['Iteración', 'x', 'f(x)', 'error'])
print(df)
print(message)
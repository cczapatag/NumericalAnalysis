import pandas as pd

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
    if not callable(f):
        raise TypeError("El argumento 'f' debe ser una función.")
    if not callable(df):
        raise TypeError("El argumento 'df' debe ser una función.")
    if not callable(df2):
        raise TypeError("El argumento 'df2' debe ser una función.")
    if not isinstance(x0, (int, float)):
        raise TypeError("El argumento 'x0' debe ser un número.")
    if not isinstance(tol, (int, float)) or tol <= 0:
        raise ValueError("El argumento 'tol' debe ser un número positivo.")
    if not isinstance(max_iterations, int) or max_iterations <= 0:
        raise ValueError(
            "El argumento 'max_iterations' debe ser un entero positivo.")

    results = []
    fx = f(x0)
    dfx = df(x0)
    df2x = df2(x0)
    iteration = 0
    error = tol + 1
    results.append([iteration, x0, fx, float('nan')])
    
    while fx != 0 and dfx != 0 and error > tol and iteration < max_iterations:
        numerator = fx * dfx
        denominator = dfx**2 - fx * df2x
        x1 = x0 - numerator / denominator
        fx = f(x1)
        dfx = df(x1)
        df2x = df2(x1)
        error = abs(x1 - x0)
        iteration += 1
        results.append([iteration, x1, fx, error])
        
        x0 = x1

    if fx == 0:
        return results, f"{x0} es raíz"
    elif error <= tol:
        return results, f"{x0} se aproxima a una raíz con una tolerancia de {tol}"
    else:
        return results, "Se alcanzó el número máximo de iteraciones"
    
#Ejemplo de uso
def f(x):
    return x**3 - x**2 - x - 1

def df(x):
    return 3*x**2 - 2*x - 1

def df2(x):
    return 6*x - 2

results, message = multiple_roots(f, df, df2, -3, 0.01, 100)
df = pd.DataFrame(results, columns=['Iteración', 'x', 'f(x)', 'error'])
print(df)
print(message)
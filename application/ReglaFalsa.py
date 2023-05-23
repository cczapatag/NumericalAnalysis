import pandas as pd
import numpy as np
def false_position(f, x_lower, x_upper, tol, max_iterations, t_error):
    """
    Encuentra una raíz de la función f(x) en el intervalo [x_lower, x_upper] usando el método de la regla falsa.

    Args:
        f: Función que se evalúa.
        x_lower: Límite inferior del intervalo en el que se busca la raíz.
        x_upper: Límite superior del intervalo en el que se busca la raíz.
        tol: Tolerancia para el error relativo o absoluto. Debe ser un número positivo.
        max_iterations: Número máximo de iteraciones a realizar. Debe ser un entero positivo.
        t_error: Indica si se debe calcular el error relativo (t_error=1) o absoluto (t_error=0).

    Returns:
        Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
        donde cada lista contiene el número de iteración, el límite inferior del intervalo, el límite superior del
        intervalo, el valor de x en el que se evalúa f(x), el valor de f(x) y el error relativo o absoluto. El segundo
        elemento es un mensaje indicando si se encontró una raíz o si se alcanzó el número máximo de iteraciones.
    """
    if not callable(f):
        raise TypeError("El argumento 'f' debe ser una función.")
    if not isinstance(x_lower, (int, float)):
        raise TypeError("El argumento 'x_lower' debe ser un número.")
    if not isinstance(x_upper, (int, float)):
        raise TypeError("El argumento 'x_upper' debe ser un número.")
    if not isinstance(tol, (int, float)) or tol <= 0:
        raise ValueError("El argumento 'tol' debe ser un número positivo.")
    if not isinstance(max_iterations, int) or max_iterations <= 0:
        raise ValueError(
            "El argumento 'max_iterations' debe ser un entero positivo.")
    if t_error not in [0, 1]:
        raise ValueError("El argumento 't_error' debe ser 0 o 1.")

    results = []
    fx_lower = f(x_lower)
    fx_upper = f(x_upper)
    if fx_lower == 0:
        return [], f"{x_lower} es raíz"
    elif fx_upper == 0:
        return [], f"{x_upper} es raíz"
    elif fx_lower * fx_upper < 0:
        x = (x_lower * fx_upper - x_upper * fx_lower) / (fx_upper - fx_lower)
        fx = f(x)
        iteration = 1
        error = tol + 1
        results.append([iteration, x_lower, x_upper, x, fx, float('nan')])
        while fx != 0 and error > tol and iteration < max_iterations:
            if fx_lower * fx < 0:
                x_upper = x
                fx_upper = fx
            else:
                x_lower = x
                fx_lower = fx
            x_prev = x
            x = (x_lower * fx_upper - x_upper * fx_lower) / (fx_upper - fx_lower)
            fx = f(x)
            if t_error == 1:
                error = abs((x - x_prev) / x)
            else:
                error = abs(x - x_prev)
            iteration += 1
            results.append([iteration, x_lower, x_upper, x, fx, error])
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
    return -7*np.log(x)+x-2

results, message = false_position(f, 20, 50, 1e-05, 100, 1)
df = pd.DataFrame(results, columns=['Iteración', 'x_lower', 'x_upper', 'x', 'f(x)', 'error'])
print(df)
print(message)
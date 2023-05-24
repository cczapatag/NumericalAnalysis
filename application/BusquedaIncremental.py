import pandas as pd

def incremental_search(f, x_init, delta_x, num_iterations):
    """
    Encuentra los intervalos en los que f(x) cambia de signo usando el método de búsqueda incremental.

    Args:
        f: Función que se evalúa.
        x_init: Valor inicial para comenzar la búsqueda.
        delta_x: Tamaño del paso para incrementar x en cada iteración. Debe ser positivo.
        num_iterations: Número de iteraciones a realizar. Debe ser un entero positivo.

    Returns:
        Una tupla con dos elementos. El primer elemento es una lista de tuplas, donde cada tupla contiene el número de
        iteración, el límite inferior y el límite superior del intervalo en el que f(x) cambia de signo. El segundo
        elemento es un mensaje indicando si se encontraron intervalos o si no se encontraron intervalos en el número
        máximo de iteraciones.
    """
    if not callable(f):
        raise TypeError("El argumento 'f' debe ser una función.")
    if not isinstance(x_init, (int, float)):
        raise TypeError("El argumento 'x_init' debe ser un número.")
    if not isinstance(delta_x, (int, float)):
        raise TypeError("El argumento 'delta_x' debe ser un número.")
    if delta_x <= 0:
        raise ValueError("El argumento 'delta_x' debe ser positivo.")
    if not isinstance(num_iterations, int) or num_iterations <= 0:
        raise ValueError(
            "El argumento 'num_iterations' debe ser un entero positivo.")
    intervals = []
    x = x_init
    fx = f(x)
    for i in range(1, num_iterations):
        x_new = x + delta_x
        fx_new = f(x_new)
        if fx * fx_new <= 0:
            intervals.append((i, x, x_new))
        x = x_new
        fx = fx_new
        if fx == 0:
            intervals.append((i, x_new, x_new))
            x = x_new
            fx = f(x)
    if intervals:
        message = "Se encontraron intervalos en los que f(x) cambia de signo"
    else:
        message = "No se encontraron intervalos en los que f(x) cambia de signo en el número máximo de iteraciones"
    return intervals, message

# Ejemplo de uso
def f(x):
    return x**2 - 4

intervals, message = incremental_search(f, 0, 0.1, 100)
df = pd.DataFrame(intervals, columns=['Iteración', 'Límite inferior', 'Límite superior'])
print(df)
for i, interval in enumerate(intervals):
    print(f"Intervalo {i+1}: {interval}")
print(message)
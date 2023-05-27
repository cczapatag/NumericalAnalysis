from sympy import sympify

class NewtonRaphson():

    def newton_raphson(f, df, x0, tol, max_iterations):
        """
        Encuentra una raíz de la función f(x) utilizando el método de Newton-Raphson.

        Args:
        f: Cadena de texto que representa la función f(x) que se evalúa.
        df: Cadena de texto que representa la derivada de la función f(x).
        x0: Valor inicial para comenzar la iteración.
        tol: Tolerancia para el error absoluto entre las aproximaciones sucesivas. Debe ser un número positivo.
        max_iterations: Número máximo de iteraciones permitidas. Debe ser un entero positivo.

        Returns:
        Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
        donde cada lista contiene el número de iteración, el valor de x en la iteración actual, el valor de f(x) en la
        iteración actual y el error absoluto entre las aproximaciones sucesivas. El segundo elemento es un mensaje
        indicando si se encontró una raíz o si se alcanzó el número máximo de iteraciones.
        """

        def eval_f(x):
            return float(sympify(f).evalf(subs={sympify('x'): x}))

        def eval_df(x):
            return float(sympify(df).evalf(subs={sympify('x'): x}))

        results = []
        x = x0
        fx = eval_f(x)
        dfx = eval_df(x)
        iteration = 0
        error = tol + 1
        results.append([iteration, x, fx, float('nan')])
        while fx != 0 and dfx != 0 and error > tol and iteration < max_iterations:
            x -= fx / dfx
            fx = eval_f(x)
            dfx = eval_df(x)
            error = abs(results[-1][1] - x)
            iteration += 1
            results.append([iteration, x, fx, error])
        if fx == 0:
            return results, f"{x} is a root"
        elif error <= tol:
            return results, f"{x} is an approximation to a root with a tolerance of {tol}"
        else:
            return results, "The maximum number of iterations was reached"

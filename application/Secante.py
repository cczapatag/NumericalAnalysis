from sympy import sympify

class Secante():

    def secante(f, x0, x1, tol, max_iterations):
        """
        Encuentra una raíz de la función f(x) utilizando el método de la secante.

        Args:
        f: Cadena de texto que representa la función f(x) que se evalúa.
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

        # Define una función para evaluar la expresión matemática representada por la cadena de texto
        def eval_f(x):
            return float(sympify(f).evalf(subs={sympify('x'): x}))

        results = []
        fx0 = eval_f(x0)
        fx1 = eval_f(x1)
        iteration = 0
        error = tol + 1
        results.append([iteration, x0, fx0, float('nan')])
        iteration += 1
        results.append([iteration, x1, fx1, abs(x1 - x0)])
 
        while fx1 != 0 and error > tol and iteration < max_iterations:
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            fx2 = eval_f(x2)
            error = abs(x2 - x1)
            iteration += 1
            results.append([iteration, x2, fx2, error])
 
            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = fx2

        if fx1 == 0:
            return results, f"{x1} is a root"
        elif error <= tol:
            return results, f"{x1} is an approximation to a root with a tolerance of {tol}"
        else:
            return results, "The maximum number of iterations was reached"
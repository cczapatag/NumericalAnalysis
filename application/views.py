from django.shortcuts import render
from application.Biseccion import Biseccion

# Create your views here.

def home(request):
    return render(request, 'index.html')

def bisection(request):

    resultado = mensaje = datos = None

    if request.POST:
        funcion = request.POST['funcion']
        intervaloA = request.POST['intervaloA']
        intervaloB = request.POST['intervaloB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        intervaloA = int(intervaloA)
        intervaloB = int(intervaloB)
        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)

        datos = {
            'fun' : funcion,
            'a' : intervaloA,
            'b' : intervaloB,
            'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
            'iter' : iteraciones
        }

        funcion = funcion.replace('^', '**')

        resultado, mensaje = Biseccion.bisection(funcion, intervaloA, intervaloB, tolerancia, iteraciones)

    return render(request, 'bisection.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def false_position(request):
    return render(request, 'false-position.html')

def fixed_point(request):
    return render(request, 'fixed-point.html')

def gauss_seidel(request):
    return render(request, 'gauss-seidel.html')

def jacobi(request):
    return render(request, 'jacobi.html')

def multiple_roots(request):
    return render(request, 'multiple-roots.html')

def newton(request):
    return render(request, 'newton-raphson.html')

def secant(request):
    return render(request, 'secant.html')

def sor(request):
    return render(request, 'sor.html')


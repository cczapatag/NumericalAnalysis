from django.shortcuts import render
from application.Biseccion import Biseccion
from application.ReglaFalsa import ReglaFalsa
from application.PuntoFijo import PuntoFijo

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

        if intervaloA < intervaloB:

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
        
        else:

            mensaje = f'Error: \'a\' has to be less than \'b\': a = {intervaloA} and b = {intervaloB}'

    return render(request, 'bisection.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def false_position(request):
    
    resultado = mensaje = datos = None

    if request.POST:
        funcion = request.POST['funcion']
        intervaloA = request.POST['intervaloA']
        intervaloB = request.POST['intervaloB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        intervaloA = int(intervaloA)
        intervaloB = int(intervaloB)

        if intervaloA < intervaloB:

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

            resultado, mensaje = ReglaFalsa.false_position(funcion, intervaloA, intervaloB, tolerancia, iteraciones)
        
        else:

            mensaje = f'Error: \'a\' has to be less than \'b\': a = {intervaloA} and b = {intervaloB}'

    return render(request, 'false-position.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def fixed_point(request):

    resultado = mensaje = datos = None

    if request.POST:
        funcionf = request.POST['funcionf']
        funciong = request.POST['funciong']   
        x0 = request.POST['x0']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        x0 = float(x0)
        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)

        datos = {
            'funf' : funcionf,
            'fung' : funciong,
            'x0' : x0,
            'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
            'iter' : iteraciones
        }

        funcionf = funcionf.replace('^', '**')
        funciong = funciong.replace('^', '**')

        resultado, mensaje = PuntoFijo.fixed_point(funcionf, funciong, x0, tolerancia, iteraciones)

    return render(request, 'fixed-point.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

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


from django.shortcuts import render
from application.Biseccion import Biseccion
from application.ReglaFalsa import ReglaFalsa
from application.PuntoFijo import PuntoFijo
from application.Jacobi import Jacobi
from application.Gauss import Seidel
from application.sor import SOR

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
        
    resultado = mensaje = datos = None

    if request.POST:

        matrizA = request.POST['matrizA']
        x0 = request.POST['x0']
        matrizB = request.POST['matrizB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)

        try:
            matrizA = matriz(matrizA)
            x0 = matriz1(x0)
            matrizB = matriz1(matrizB)

            if size(matrizA) and size(x0) and size(matrizB) and len(matrizA) == len(x0) and len(matrizA) == len(matrizB):
                
                datos = {
                    'matrizA' : matrizA,
                    'matrizB' : matrizB,
                    'x0' : x0,
                    'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
                    'iter' : iteraciones,
                }

                resultado, mensaje = Seidel.seidel(matrizA, matrizB, x0, iteraciones, tolerancia)

            else:
                mensaje = "The matrixes had different sizes."

        except:
            mensaje = "An error has occurred on the input."

    return render(request, 'gauss-seidel.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def jacobi(request):

    resultado = mensaje = datos = None

    if request.POST:

        matrizA = request.POST['matrizA']
        x0 = request.POST['x0']
        matrizB = request.POST['matrizB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)

        try:

            matrizA = matriz(matrizA)

            x0 = matriz1(x0)

            matrizB = matriz1(matrizB)

            if size(matrizA) and size(x0) and size(matrizB) and len(matrizA) == len(x0) and len(matrizA) == len(matrizB):
                
                datos = {
                    'matrizA' : matrizA,
                    'matrizB' : matrizB,
                    'x0' : x0,
                    'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
                    'iter' : iteraciones,
                }

                resultado, mensaje = Jacobi.jacobi(matrizA, matrizB, x0, iteraciones, tolerancia)

            else:
                mensaje = "The matrixes had different sizes."

        except:
            mensaje = "An error has occurred on the input."

    return render(request, 'jacobi.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def multiple_roots(request):
    return render(request, 'multiple-roots.html')

def newton(request):
    return render(request, 'newton-raphson.html')

def secant(request):
    return render(request, 'secant.html')

def sor(request):
            
    resultado = mensaje = datos = None

    if request.POST:

        matrizA = request.POST['matrizA']
        x0 = request.POST['x0']
        matrizB = request.POST['matrizB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']
        w = request.POST['relax']

        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)
        w = float(w)

        try:
            matrizA = matriz(matrizA)
            x0 = matriz1(x0)
            matrizB = matriz1(matrizB)

            if size(matrizA) and size(x0) and size(matrizB) and len(matrizA) == len(x0) and len(matrizA) == len(matrizB):

                datos = {
                    'matrizA' : matrizA,
                    'matrizB' : matrizB,
                    'x0' : x0,
                    'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
                    'iter' : iteraciones,
                    'relajacion' : w
                }

                resultado, mensaje = SOR.sor(matrizA, matrizB, x0, w, tolerancia, iteraciones)

            else:
                mensaje = "The matrixes had different sizes."

        except:
            mensaje = "An error has occurred on the input."

    return render(request, 'sor.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def matriz(mtz):

    mtz = mtz.split(' ')

    arr = []
    arr2 = []

    i = 0
    while i < len(mtz):
        if mtz[i] == ';':
            arr.append(arr2)
            arr2 = []
            i += 1
            continue

        arr2.append(float(mtz[i]))
        i += 1

    arr.append(arr2)

    return arr

def matriz1(mtz):
    
    mtz = mtz.split(' ')

    arr = []

    i = 0
    while i < len(mtz):
        arr.append(float(mtz[i]))
        i += 2

    return arr

def size(mtz):
    try:
        subarray_sizes = [len(subarr) for subarr in mtz]
        return all(size == subarray_sizes[0] for size in subarray_sizes)
    except:
        return True
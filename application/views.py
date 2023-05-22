from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def bisection(request):
    return render(request, 'bisection.html')

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


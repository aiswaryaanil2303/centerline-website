from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'service.html')


def hvac(request):
    return render(request, 'hvac.html')


def modular_construction(request):
    return render(request, 'modular-construction.html')


def infection_control(request):
    return render(request, 'infection-control.html')


def medical_gas(request):
    return render(request, 'medical-gas.html')


def hospital_electrical(request):
    return render(request, 'hospital-electrical.html')

def solutions(request):
    return render(request, 'solution.html')

def clients(request):
    return render(request, 'clients.html')

def contact(request):
    return render(request, 'contact.html')
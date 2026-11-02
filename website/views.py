from django.shortcuts import render

# Create your views
def home(request):
    return render(request, 'home.html')
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

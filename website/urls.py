
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),

    path('services/hvac/', views.hvac, name='hvac'),
    path('services/modular-construction/', views.modular_construction, name='modular_construction'),
    path('services/infection-control/', views.infection_control, name='infection_control'),
    path('services/medical-gas/', views.medical_gas, name='medical_gas'),
    path('services/hospital-electrical/', views.hospital_electrical, name='hospital_electrical'),

    path('solutions/', views.solutions, name='solutions'),
    path('clients/', views.clients, name='clients'),
    path('contact/', views.contact, name='contact'),
]


from django.urls import path

from . import views

urlpatterns = [
    path('services_computer_wizard/', views.service_views(), name = 'service_views'),

]
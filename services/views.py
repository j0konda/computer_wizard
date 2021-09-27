

# проверка или удалятся файлы закинутые вручную на сервере
from django.shortcuts import render

from services.models import ServiceComputer

def service_views(request):
    servicesComputer= ServiceComputer.objects.all()
    context = {'servicesComputer': servicesComputer }
    return render(request, '/services_computer_wizard.html', context)



# Create your views here.

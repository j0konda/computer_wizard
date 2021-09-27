from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

import services
from . import views

urlpatterns = [
    path('services_computer_wizard/', views.service_views, name = 'service_views'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
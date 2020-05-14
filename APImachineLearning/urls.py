from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pacientes.api.viewsets import PacientViewSet, TreinarRNA

#router = routers.DefaultRouter()
#router.register(r'paciente', PacientViewSet)

urlpatterns = [
    path('', PacientViewSet.as_view()),
    path('treinar/', TreinarRNA.as_view()),
    path('admin/', admin.site.urls),
]

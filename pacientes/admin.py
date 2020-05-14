from django.contrib import admin
from .models import Pacient

class PacientAdmin(admin.ModelAdmin):
	list_display = ['nome', 'febreModerada','febreAlta',
	                'tossePersistente', 'tosseSeca', 'faltaDeAr',
	                'dificuldadeRespirar', 'problemaGastrico',
	                'diarreia', 'suspeitaCorona']

admin.site.register(Pacient, PacientAdmin)
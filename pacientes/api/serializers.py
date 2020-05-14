from rest_framework.serializers import ModelSerializer
from pacientes.models import Pacient

class PacientSerializer(ModelSerializer):
	class Meta:
		model = Pacient
		fields = ['nome', 'febreModerada', 'febreAlta', 'tossePersistente', 'tosseSeca', 'faltaDeAr',
		          'dificuldadeRespirar', 'problemaGastrico', 'diarreia', 'suspeitaCorona']
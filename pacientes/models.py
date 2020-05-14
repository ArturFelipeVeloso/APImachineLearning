from django.db import models
import json

# Create your models here.
class Pacient(models.Model):
    nome = models.CharField(max_length=200)
    febreModerada = models.IntegerField()
    febreAlta = models.IntegerField()
    tossePersistente = models.IntegerField()
    tosseSeca = models.IntegerField()
    faltaDeAr = models.IntegerField()
    dificuldadeRespirar = models.IntegerField()
    problemaGastrico = models.IntegerField()
    diarreia = models.IntegerField()
    suspeitaCorona = models.IntegerField(null=True)

    def getElementos(self):
        return list([self.nome, self.febreModerada, self.febreAlta, self.tossePersistente, self.tosseSeca, self.faltaDeAr, self.dificuldadeRespirar, self.problemaGastrico, self.diarreia, self.suspeitaCorona])

'''
class Modelo(models.Models):
    nome = models.CharField(max_length=200)
    data = models.CharField(max_length=120, default="[]")

    def set_data(self, x):
        self.data = json.dumps(x)

    def get_data(self):
        return json.loads(self.data)
'''
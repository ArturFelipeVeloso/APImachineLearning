from rest_framework.viewsets import ModelViewSet
from pacientes.models import Pacient
from .serializers import PacientSerializer
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier

modelo = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(1024, 128),
                               random_state=1, max_iter=150)

primeiroAcesso = 0

class TreinarRNA(APIView):
    def get(self, request, format=None):
        Pacients = Pacient.objects.all()

        print(Pacients)
        allPacients = []
        for p in Pacients:
            allPacients.append(p.getElementos())

        resposta = []
        for i, d in enumerate(allPacients):
            resposta.append(d[-1])
            allPacients[i].pop()
            allPacients[i].pop(0)

        print(allPacients)
        print(resposta)
        modelo.fit(allPacients, resposta)
        print("RNA Treinada!")

        serializer = PacientSerializer(Pacients, many=True)
        return Response(serializer.data)

class PacientViewSet(APIView):

    def get(self, request, format=None):
        Pacients = Pacient.objects.all()
        serializer = PacientSerializer(Pacients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = PacientSerializer(data=request.data)

        if serializer.is_valid():
            #if super.primeiroAcesso == 0:
                #TreinarRNA.get()
                #super.primeiroAcesso = 1
            '''
            ### MACHINE LEARNING
            Pacients = Pacient.objects.all()

            print(Pacients)
            allPacients = []
            for p in Pacients:
                allPacients.append(p.getElementos())

            resposta = []
            for i, d in enumerate(allPacients):
                resposta.append(d[-1])
                allPacients[i].pop()
                allPacients[i].pop(0)

            print(allPacients)
            print(resposta)

            # Naive Bayes
            #modelo = MultinomialNB()
            #modelo.fit(allPacients, resposta)

            #RNA
            modelo = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(1024, 128),
                                   random_state=1, max_iter=150)
            modelo.fit(allPacients, resposta)
            '''
            febreModerada = serializer.validated_data.get('febreModerada'),
            febreAlta = serializer.validated_data.get('febreAlta'),
            tossePersistente = serializer.validated_data.get('tossePersistente'),
            tosseSeca = serializer.validated_data.get('tosseSeca'),
            faltaDeAr = serializer.validated_data.get('faltaDeAr'),
            dificuldadeRespirar = serializer.validated_data.get('dificuldadeRespirar'),
            problemaGastrico = serializer.validated_data.get('problemaGastrico'),
            diarreia = serializer.validated_data.get('diarreia')

            newPacient = [febreModerada[0], febreAlta[0], tossePersistente[0],
                          tosseSeca[0], faltaDeAr[0], dificuldadeRespirar[0],
                          problemaGastrico[0], diarreia]
            print(newPacient)
            if modelo.predict([newPacient]) == 1:
                print("Paciente com risco de corona.")
                suspeitaCorona = 1
            else:
                print("Paciente não apresenta sintomas do corona.")
                suspeitaCorona = 0

            serializer.validated_data['suspeitaCorona'] = suspeitaCorona
            serializer.save()
            print(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #queryset = Pacient.objects.all()
    #serializer_class = PacientSerializer
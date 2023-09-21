# disciplinas/views.py
from rest_framework import generics
from atividade.models import Disciplina
from atividade.serializers.disciplinaSerializer import DisciplinaSerializer

"""
Views para listar, criar, detalhar, atualizar e excluir objetos Disciplina usando o serializador DisciplinaSerializer.
"""


class DisciplinaListCreateView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class DisciplinaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
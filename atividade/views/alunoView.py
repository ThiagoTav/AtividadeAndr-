# disciplinas/views.py
from rest_framework import generics
from atividade.models import Aluno
from atividade.serializers.alunoSerializer import AlunoSerializer

"""
Views para listar, criar, detalhar, atualizar e excluir objetos Aluno usando o serializador AlunoSerializer.
"""


class AlunoListCreateView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
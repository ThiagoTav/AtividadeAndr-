# disciplinas/views.py
from rest_framework import generics
from atividade.models import Tarefa
from atividade.serializers.tarefaSerializer import TarefaSerializer

"""
Views para listar, criar, detalhar, atualizar e excluir objetos Tarefa usando o serializador TarefaSerializer.
"""


class TarefaListCreateView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TarefaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
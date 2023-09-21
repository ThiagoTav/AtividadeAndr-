# disciplinas/serializers.py
from rest_framework import serializers
from atividade.models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    """
Serializador para o modelo Tarefa (converte objetos Tarefa em JSON e vice-versa).
"""

    class Meta:
        model = Tarefa
        fields = '__all__'
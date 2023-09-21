# disciplinas/serializers.py
from rest_framework import serializers
from atividade.models import Disciplina

class DisciplinaSerializer(serializers.ModelSerializer):
    """
Serializador para o modelo Disciplina(converte objetos Disciplina em JSON e vice-versa).
"""

    class Meta:
        model = Disciplina
        fields = '__all__'
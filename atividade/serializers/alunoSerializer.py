# disciplinas/serializers.py
from rest_framework import serializers
from atividade.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    """
Serializador para o modelo Aluno (converte objetos Aluno em JSON e vice-versa).
"""
    class Meta:
        model = Aluno
        fields = '__all__'

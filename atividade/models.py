from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField(default=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.titulo


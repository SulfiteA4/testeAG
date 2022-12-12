from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=150)
    telefone =models.CharField(max_length=11)
    cnh = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=100)
    modelo_veiculo = models.CharField(max_length=100)
    km_troca_oleo = models.CharField(max_length=10)

    def __str__(self):
        return self.modelo_veiculo

class Controle(models.Model):
    veiculo = models.ForeignKey('Veiculo', on_delete=models.CASCADE)
    motorista = models.ForeignKey('Motorista', on_delete=models.CASCADE)
    data_saida = models.DateField(auto_now=False)
    hora_saida = models.TimeField(auto_now=False)
    km_saida = models.CharField(max_length=10)
    destino = models.CharField(max_length=150) #endereco?
    data_retorno = models.DateField(auto_now=False)
    hora_retorno = models.TimeField(auto_now=False)
    km_retorno = models.CharField(max_length=10)
    km_percorrido = models.CharField(max_length=10)
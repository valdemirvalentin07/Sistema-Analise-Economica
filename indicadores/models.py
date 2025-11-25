from django.db import models

class Indicador(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    percentual_lucro = models.DecimalField(max_digits=5, decimal_places=2)  # ex: 20 para 20%
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.categoria})"
    
    @property
    def valor_total(self):
        """Retorna o valor total considerando a quantidade"""
        return self.valor * self.quantidade

    @property
    def lucro_total(self):
        """Retorna o lucro total considerando percentual"""
        return self.valor_total * (self.percentual_lucro / 100)

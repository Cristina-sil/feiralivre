from django.db import models

from produtos.models import Frutas, Verduras


class Entrega(models.Model):
    nmClnt = models.CharField(max_length=255)
    endrNtrg = models.TextField()
    dtEntrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')

class Item(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nmItm = models.CharField(max_length=100)
    qntdd = models.IntegerField()
    prcUnit = models.DecimalField(max_digits=6, decimal_places=2)


# Create your models here.

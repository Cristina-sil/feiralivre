from django.db import models


class Pagamento(models.Model):
    mtPgto = models.CharField(max_length=50)
    vlrTotal = models.DecimalField(max_digits=8, decimal_places=2)
    
# Create your models here.

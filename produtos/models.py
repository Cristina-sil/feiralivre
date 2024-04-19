from django.db import models


class Verduras(models.Model):
    nmVdx = models.CharField(max_length=100)
    pXcVdX = models.DecimalField(max_digits=6, decimal_places=2)
    stkVxL = models.IntegerField()

class Frutas(models.Model):
    nmeFrt = models.CharField(max_length=100)
    prcFrt = models.DecimalField(max_digits=6, decimal_places=2)
    qntdDspnvl = models.IntegerField()
    
# Create your models here.

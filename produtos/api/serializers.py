from rest_framework import serializers

from produtos.models import Frutas, Verduras


class VerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verduras
        fields = ['nmVdx', 'pXcVdX', 'stkVxL']

class FrutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frutas
        fields = ['nmeFrt', 'prcFrt', 'qntdDspnvl']

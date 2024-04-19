from rest_framework import serializers

from .models import Entrega, Item, Pagamento


class EntregaSerializer(serializers.ModelSerializer):
    itens = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    pagamento = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all())

    class Meta:
        model = Entrega
        fields = ['nmClnt', 'endrNtrg', 'dtEntrega', 'itens', 'pagamento']

class ItemSerializer(serializers.ModelSerializer):
    entrega = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())

    class Meta:
        model = Item
        fields = ['nmItm', 'qntdd', 'prcUnit', 'entrega']

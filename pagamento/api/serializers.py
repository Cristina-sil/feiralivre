from rest_framework import serializers

from pagamento.models import Pagamento


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['mtPgto', 'vlrTotal']

from rest_framework import viewsets

from pagamento.api.serializers import PagamentoSerializer
from pagamento.models import Pagamento


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'message': 'Pagamento excluído com sucesso!'})

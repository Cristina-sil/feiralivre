from pagamentos.api.serializers import PagamentoSerializer
from rest_framework import viewsets

from app.models import Pagamento


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'message': 'Pagamento excluído com sucesso!'})

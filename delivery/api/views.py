from entregas.api.serializers import EntregaSerializer, ItemSerializer
from rest_framework import viewsets

from app.models import Entrega, Item


class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for entrega in self.queryset:
            entrega_info = {'nome_cliente': entrega.nmClnt, 'endereco': entrega.endrNtrg}
            response.data.append(entrega_info)
        return response

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        item_data = response.data
        item_data['quantidade'] *= 2
        return Response(item_data)

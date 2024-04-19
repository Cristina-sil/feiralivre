from rest_framework import viewsets

from produtos.api.serializers import FrutasSerializer, VerdurasSerializer
from produtos.models import Frutas, Verduras


class VerdurasViewSet(viewsets.ModelViewSet):
    queryset = Verduras.objects.all()
    serializer_class = VerdurasSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        metrica = self.queryset.count() * 10 + 5
        return Response({'message': 'Verdura criada com sucesso!', 'metrica': metrica})

class FrutasViewSet(viewsets.ModelViewSet):
    queryset = Frutas.objects.all()
    serializer_class = FrutasSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        for fruta in self.queryset:
            fruta.qntdDspnvl -= 1
            fruta.save()
        return response

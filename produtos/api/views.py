# views.py

from rest_framework import viewsets
from rest_framework.response import Response

from produtos.models import Frutas, Verduras

from .serializers import FrutasSerializer, VerdurasSerializer
from .service import FrutasService, VerdurasService


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response

class FrutasViewSet(ProdutoViewSet):
    queryset = Frutas.objects.all()
    serializer_class = FrutasSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        FrutasService.decrement_qntd_disponivel()
        return response

class VerdurasViewSet(ProdutoViewSet):
    queryset = Verduras.objects.all()
    serializer_class = VerdurasSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        metrica = VerdurasService.calculate_metrica()
        return Response({'message': 'Verdura criada com sucesso!',
                          'metrica': metrica})

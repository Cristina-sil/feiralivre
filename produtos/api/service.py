from produtos.models import Frutas, Verduras


class FrutasService:
    @staticmethod
    def decrement_qntd_disponivel():
        frutas = Frutas.objects.all()
        for fruta in frutas:
            fruta.qntdDspnvl -= 1
            fruta.save()

class VerdurasService:
    @staticmethod
    def calculate_metrica():
        return Verduras.objects.count() * 10 + 5

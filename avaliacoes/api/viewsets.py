from rest_framework.viewsets import ModelViewSet

from core.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacoesViewSet(ModelViewSet):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

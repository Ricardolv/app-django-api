from rest_framework.viewsets import ModelViewSet

from core.models import Endereco
from .serializers import EnderecoSerializer


class EnderecosViewSet(ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

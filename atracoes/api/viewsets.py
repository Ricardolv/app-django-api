from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Atracao
from .serializers import AtracaoSerializer

from django_filters import rest_framework as filters


class AtracaoFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name="nome", lookup_expr='icontains')
    descricao = filters.CharFilter(field_name="descricao", lookup_expr='icontains')


class Meta:
    model = Atracao
    fields = ['nome', 'descricao', ]


class AtracaoViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AtracaoFilter

from rest_framework.viewsets import ModelViewSet

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

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AtracaoFilter

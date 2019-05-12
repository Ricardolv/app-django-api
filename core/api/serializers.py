from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    endereco = EnderecoSerializer()
    decrisao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'decrisao_completa', 'descricao_completa2')

    def get_decrisao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)

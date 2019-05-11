from django.contrib import admin
from avaliacoes.models import Avaliacao


class AvaliacaoAdmin(admin.ModelAdmin):
    list_filter = ('usuario', 'nota', 'data')
    list_display = ('id', 'usuario', 'comentario', 'nota', 'data')
    search_fields = ('id', 'usuario', 'comentario', 'nota', 'data')


admin.site.register(Avaliacao, AvaliacaoAdmin)
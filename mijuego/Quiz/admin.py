from Quiz.forms import ElegirInlineFormSet
from django.contrib import admin
from django.db import models
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas,QuizUsuario

class ElegirRespuestaInline(admin.TabularInline):
    model=ElegirRespuesta
    can_delete=False
    max_num=ElegirRespuesta.MAXIMO_RESPUESTA
    min_num=ElegirRespuesta.MAXIMO_RESPUESTA
    formset=ElegirInlineFormSet

class PreguntaAdmin(admin.ModelAdmin):
    model=Pregunta
    inlines=(ElegirRespuestaInline,)
    list_display=['texto',]
    search_fields=['texto', 'preguntas__texto',]

class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display= ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']


class Meta:
    model=PreguntasRespondidas


admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(QuizUsuario)

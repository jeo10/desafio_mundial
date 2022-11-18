from rest_framework import serializers
from apps.mundial_predict.models import *


class SeleccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seleccion
        fields = '__all__'


class PartidoSerializer(serializers.ModelSerializer):
    equipo1 = SeleccionSerializer()
    equipo2 = SeleccionSerializer()

    class Meta:
        model = Partido
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'codigo_partido': instance.codigo_partido,
            'fecha': instance.fecha,
            'horario': instance.horario,
            'estadio': instance.estadio,
            'fase': instance.fase,
            'fase_desc': instance.fase_desc,
            'equipo1_cod': '' if instance.fase != 'Grupos' else instance.equipo1.codigo_seleccion,
            'equipo1_nombre': '' if instance.fase != 'Grupos' else instance.equipo1.nombre,
            'equipo2_cod': '' if instance.fase != 'Grupos' else instance.equipo2.codigo_seleccion,
            'equipo2_nombre': '' if instance.fase != 'Grupos' else instance.equipo2.nombre
        }


class PrediccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prediccion
        fields = '__all__'

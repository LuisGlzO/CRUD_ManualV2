from rest_framework import serializers
from .models import Persona, Salones

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombre', 'apellido', 'correo']
    """
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.correo = validated_data.get('correo', instance.correo)

        instance.save()
        return instance
    """
class SalonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salones
        fields = ['id', 'nombre', 'edificio', 'capacidad']
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PersonaSerializer, SalonSerializer
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from .models import Persona, Salones
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters
# Create your views here.

class PersonaAPI(APIView):
    def get(self, request, format=None):
        #personas = [Persona.nombre for persona in Persona.objects.all()]
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PersonaDetail(ListView):

    def get(self, request, persona_id):
        persona = Persona.objects.get(id=persona_id)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)


    def put(self, request, persona_id):
        print(persona_id)
        persona = Persona.objects.get(id=persona_id)
        print(persona)
        print(request.data)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, persona_id):
        persona = Persona.objects.get(id=persona_id)
        persona.delete()
        return Response({"message" :" Persona eliminada"}, status=status.HTTP_200_OK)

class Extra(APIView):
    def get(self, request, persona_nombre):
        persona = Persona.objects.get(nombre=persona_nombre)
        serializer = PersonaSerializer(persona, many = True)
        return Response({"data":serializer.data})

class PersonaListView(ListAPIView):
    filter_backends = [DjangoFilterBackend]
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']
    """
    def put(self, request, persona_id):
        personaGuardada = get_object_or_404(Persona.objects.all(), pk=pk)
        data = request.data.get('Persona')
        serializer = PersonaSerializer(instance=personaGuardada, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            personaGuardada = serializer.save()
        return Response({"success": "Persona '{}' updated successfully".format(personaGuardada.nombre)})
    
    def personaDetail(self, request, persona_id):

        try:
            persona = Persona.objects.get(id=persona_id)
        except persona.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = PersonaSerializer(persona, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            persona.delete()
            return Response({"message" :" Persona eliminada"}, status=status.HTTP_200_OK)
   
    """
class SalonesAPI(APIView):

    def get(self, request, format=None):
        salones = Salones.objects.all()
        serializer = SalonSerializer(salones, many = True)
        return Response({"data":serializer.data})

    def post(self, request):
        serializer = SalonSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class SalonesDetail(APIView):

    def get(self, request, salon_id):
        salon = Salones.objects.get(id=salon_id)
        serializer = SalonSerializer(salon)
        return Response(serializer.data)


    def put(self, request, salon_id):
        print(salon_id)
        salon = Salones.objects.get(id=salon_id)
        print(salon)
        print(request.data)
        serializer = SalonSerializer(salon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, salon_id):
        salon = Salones.objects.get(id=salon_id)
        salon.delete()
        return Response({"message" :" salon eliminado"}, status=status.HTTP_200_OK)
    
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators import csrf
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import MaestroProducto
from .serializers import MaestroProductoSerializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MaestroProducto_create(APIView):
    def post(self, request, format=None):
        serializer = MaestroProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaestroProducto_update(APIView):
    def put(self, request, format=None):
        serializer = MaestroProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def MaestroProducto_read(request, id):
    if request.method == 'GET':
        objeto = get_object_or_404(MaestroProducto, patente=id)
        serializer = MaestroProductoSerializers(objeto)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def MaestroProducto_read_all(request):
    if request.method == 'GET':
        list = MaestroProducto.objects.all()
        serializer = MaestroProductoSerializers(list, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def MaestroProducto_delete(request, id):
    if request.method == 'DELETE':
        try:
            MaestroProducto.objects.get(patente=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MaestroProducto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    password_valida = check_password(password, user.password)
    if not password_valida:
        return Response("Contraseña incorrecta")
    token, created = Token.objects.get_or_create(user=user)
    print(f"Este es el token creado: '{token.key}'")
    return Response(token.key)


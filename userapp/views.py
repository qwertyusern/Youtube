from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from asosiy.serializers import KanalSer,UserSer
class Users(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

class UserGet(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer


class KanalApi(APIView):
    def get(self, request, pk):
        k=Kanal.objects.get(id=pk)
        ser = KanalSer(k)
        return Response(ser.data)
    def put(self, request, pk):
        u = User.objects.get(username=request.user.username)
        kanal = Kanal.objects.get(id=pk)
        if kanal.user == u:
            malumot = request.data
            ser = KanalSer(kanal,data=malumot)
            if ser.is_valid():
                ser.save(user=u)
            return Response(ser.data)
        return Response()

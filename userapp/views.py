from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from asosiy.serializers import KanalSer,UserSer
class Users(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

class UserGet(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer


class KanalV(generics.RetrieveUpdateAPIView):
    queryset = Kanal.objects.all()
    serializer_class = KanalSer
    def update(self, request,pk):
        k = Kanal.objects.get(user=self.request.user)
        if k.user==self.request.user:
            k=Kanal.objects.get(id=pk).update()
            serializer = KanalSer(k,data=self.request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response()

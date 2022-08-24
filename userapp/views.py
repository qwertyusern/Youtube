from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from asosiy.serializers import UserSer,AccountSer,ConnectionSer
class Users(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

class UserGet(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer


class AccountView(generics.RetrieveUpdateAPIView):
    queryset=Account.objects.all()
    serializer_class = AccountSer
    def perform_destroy(self, instance):
        if User==self.request.user:
            instance.delete()
        return Response(instance)
class Connections(generics.ListCreateAPIView):
    queryset=Connection.objects.all()
    serializer_class = ConnectionSer
    def get_queryset(self):
        queryset = []
        ism = self.request.query_params.get('follower_ism')
        if ism is not None:
            p1 = Account.objects.get(username=ism)
            queryset = Connection.objects.filter(follower_id=p1)
        f_ism = self.request.query_params.get('following_ism')
        if f_ism is not None:
            p1 = Account.objects.get(username=f_ism)
            queryset = Connection.objects.filter(following_id=p1)
        return queryset



class ConnectionDelete(generics.DestroyAPIView):
    queryset=Connection.objects.all()
    serializer_class = ConnectionSer
    def perform_destroy(self, instance):
        p1=Account.objects.get(username=self.request.user)
        if instance.following_id==p1 or instance.follower_id==p1:
            instance.delete()
        return Response(instance)

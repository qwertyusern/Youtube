from django.shortcuts import render
from .models import *
from userapp.models import Profil
from rest_framework import status, generics
from .serializers import *
from rest_framework.response import Response

class Posts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer
class Efirlar(generics.ListCreateAPIView):
    queryset = Efir.objects.all()
    serializer_class = EfirSer
class EfirGet(generics.RetrieveDestroyAPIView):
    queryset = Efir.objects.all()
    serializer_class = EfirSer
class PostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer
    def put(self,request, pk):
        p = Profil.objects.get(username=self.request.user)
        post = Post.objects.get(id=pk)
        if post.profil == p:
            ser = PostSer(post, data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()


class Medias(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer


class MediaGet(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer


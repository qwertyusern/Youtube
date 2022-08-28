from django.shortcuts import render
from rest_framework.views import APIView

from .models import *
from userapp.models import Kanal
from rest_framework import status, generics
from .serializers import *
from rest_framework.response import Response

class ReccomendApiView(generics.ListAPIView):
    queryset =Reccomend.objects.all()
    serializer_class = ReccommendSer

class VideoApiView(APIView):
    def get(self,request):
        v=Video.objects.all()
        ser=VideoSer(v,many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = VideoSer(data=malumot)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)

class VideoApi(APIView):
    def get(self, request, pk):
        v=Video.objects.get(id=pk)
        ser = VideoSer(v)
        return Response(ser.data)
    def delete(self, request,pk):
        k=Kanal.objects.get(user=self.request.user)
        v=Video.objects.get(id=pk)
        if v.kanal==k:
            malumot = request.data
            ser = EfirSer(data=malumot)
            if ser.is_valid():
                v.delete()
                ser.save()
        return Response()
class EfirApiVIew(APIView):
    def get(self,request):
        e=Efir.objects.all()
        ser=EfirSer(e,many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = EfirSer(data=malumot)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)
class EfirApi(APIView):
    def get(self, request, pk):
        e=Efir.objects.get(id=pk)
        ser = EfirSer(e)
        return Response(ser.data)
    def delete(self, request,pk):
        k=Kanal.objects.get(user=self.request.user)
        e=Efir.objects.get(id=pk)
        if e.kanal==k:
            malumot = request.data
            ser = EfirSer(data=malumot)
            if ser.is_valid():
                e.delete()
                ser.save()
        return Response()

class PlaylistApiView(APIView):
    def get(self,request):
        p=Playlist.objects.all()
        ser=PlaylistSer(p,many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = PlaylistSer(data=malumot)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)



from django.shortcuts import render
from .models import *
from userapp.models import Kanal
from rest_framework import status, generics
from .serializers import *
from rest_framework.response import Response

class ReccomendView(generics.ListAPIView):
    queryset =Reccomend.objects.all()
    serializer_class = ReccommendSer

class VideoView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSer
    def post(self, request):
        k=Kanal.objects.get(user=request.user)
        if k.user==self.request.user:
            v=Video.objects.create()
            ser = VideoSer(v,data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()

class VideoV(generics.RetrieveDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSer
    def retrieve(self, request, pk):
        k = Kanal.objects.get(user=self.request.user)
        if k.user==self.request.user:
            Video.objects.get(id=pk)
        return Response()
    def destroy(self, request,pk):
        k=Kanal.objects.get(user=self.request.user)
        if k.user==self.request.user:
            Video.objects.get(id=pk).delete()
        return Response()
class Efirlar(generics.ListCreateAPIView):
    queryset = Efir.objects.all()
    serializer_class = EfirSer
    def post(self, request):
        k = Kanal.objects.get(user=self.request.user)
        if k.user==self.request.user:
            e=Efir.objects.create()
            ser = EfirSer(e,data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()
class EfirView(generics.RetrieveDestroyAPIView):
    queryset = Efir.objects.all()
    serializer_class = EfirSer



class PlaylistView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSer
    def post(self, request):
        k=Kanal.objects.get(user=self.request.user)
        if k.user==self.request.user:
            p=Playlist.objects.create()
            ser = PlaylistSer(p, data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()



from django.shortcuts import render
from .models import *
from userapp.models import Account
from rest_framework import status, generics
from .serializers import *
from rest_framework.response import Response

class VideoView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSer
    def post(self, request):
        if Account.user==self.request.user:
            ser = VideoSer(data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()

class VideoDelete(generics.DestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSer
    def perform_destroy(self, instance):
        v = Video.objects.get(account=self.request.user)
        if v:
            instance.delete()
        return Response(instance)
class Efirlar(generics.ListCreateAPIView):
    queryset = Efir.objects.all()
    serializer_class = EfirSer
    def post(self, request):
        if Account.user==self.request.user:
            ser = EfirSer(data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()
class EfirGet(generics.RetrieveDestroyAPIView):
    queryset = Efir.objects.all()
    serializer_class = EfirSer

class KanalView(generics.ListAPIView):
    queryset = Kanal.objects.all()
    serializer_class = KanalSer

class KanalV(generics.RetrieveUpdateAPIView):
    queryset = Kanal.objects.all()
    serializer_class = KanalSer
    def partial_update(self, request, *args, **kwargs):
        if Account.user==self.request.user:
            ser = KanalSer(data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()


class PlaylistView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSer
    def post(self, request):
        if Account.user==self.request.user:
            ser = PlaylistSer( data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()



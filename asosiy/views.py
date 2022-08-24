from django.shortcuts import render
from .models import *
from userapp.models import Account
from rest_framework import status, generics
from .serializers import *
from rest_framework.response import Response

class VideoView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSer
    def put(self, request, pk):
        a = Account.objects.get(user=self.request.user)
        v = Video.objects.get(id=pk)
        if v.account == a:
            ser = VideoSer(v, data=self.request.data)
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
    def put(self, request, pk):
        e = Account.objects.get(user=self.request.user)
        efir = Efir.objects.get(id=pk)
        if efir.account == e:
            ser = EfirSer(efir, data=self.request.data)
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
        k = Kanal.objects.get(account=self.request.user)
        if k:
            ser = KanalSer(k, data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()


class PlaylistView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSer
    def put(self, request, pk):
        e = Account.objects.get(user=self.request.user)
        p = Playlist.objects.get(id=pk)
        if p.account == e:
            ser = PlaylistSer(p, data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()



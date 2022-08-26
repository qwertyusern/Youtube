from django.contrib.auth.models import User

from .models import *
from userapp.models import Kanal

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ReccommendSer(serializers.ModelSerializer):
    class Meta:
        model=Reccomend
        fields="__all__"


class CommentSer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"


class VideoSer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields="__all__"

class EfirSer(serializers.ModelSerializer):
    class Meta:
        model=Efir
        fields="__all__"


class LikeSer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields="__all__"

class KanalSer(serializers.ModelSerializer):
    class Meta:
        model=Kanal
        fields="__all__"

class PlaylistSer(serializers.ModelSerializer):
    class Meta:
        model=Playlist
        fields="__all__"

class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

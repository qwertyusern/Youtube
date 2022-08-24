from django.contrib.auth.models import User

from .models import *
from userapp.models import Account,Connection

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class AccountSer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields="__all__"

class ConnectionSer(serializers.ModelSerializer):
    follower=Account
    following=Account
    class Meta:
        model=Connection
        fields="__all__"

class CommentSer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"

class Comment_likeSer(serializers.ModelSerializer):
    class Meta:
        model=Comment_like
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

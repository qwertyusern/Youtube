from django.db import models
from userapp.models import Kanal


class Comment(models.Model):
    matn=models.CharField(max_length=500)
    sana=models.DateField(auto_now_add=True)

class Like(models.Model):
    like_soni = models.PositiveIntegerField()

class Video(models.Model):
    video=models.URLField()
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="comment_video",null=True)
    like=models.ForeignKey(Like,on_delete=models.CASCADE,related_name="like_video",null=True)
    kanal=models.ForeignKey(Kanal,on_delete=models.CASCADE,related_name="kanal_video",null=True)


class Reccomend(models.Model):
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="rec_video",)
    kanal=models.ForeignKey(Kanal,on_delete=models.CASCADE,related_name="kanal_rec",)


class Playlist(models.Model):
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="video_playlist",null=True)
    kanal=models.ForeignKey(Kanal,on_delete=models.CASCADE,related_name="playlist_kanal",null=True)


class Efir(models.Model):
    matn = models.TextField()
    koryapturganlar_soni=models.PositiveIntegerField()
    boshlangan_vaqti=models.TimeField(auto_now_add=True)
    video=models.OneToOneField(Video,on_delete=models.CASCADE,related_name="efir_video")
    kanal=models.OneToOneField(Kanal,on_delete=models.CASCADE,related_name="kanal_efir",)







from django.db import models
from userapp.models import Account,Connection


class Comment(models.Model):
    matn=models.CharField(max_length=500)
    sana=models.DateField(auto_now_add=True)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)

class Comment_like(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="comment_like",null=True)
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="comment_account",null=True)

class Video(models.Model):
    video=models.URLField()
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="comment_video",null=True)
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_video",null=True)

class Like(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_like",null=True)
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="video_like",null=True)



class Kanal(models.Model):
    nomi=models.CharField(max_length=20)
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="video_kanal",null=True)
    connection=models.ForeignKey(Connection,on_delete=models.CASCADE,related_name="connect_kanal",null=True)
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_kanal",null=True)


class Playlist(models.Model):
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="video_playlist",null=True)
    like=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="like_playlist",null=True)
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="acc_playlist",null=True)


class Efir(models.Model):
    matn = models.TextField()
    koryapturganlar_soni=models.PositiveIntegerField()
    boshlangan_vaqti=models.TimeField(auto_now_add=True)
    account=models.OneToOneField(Account,on_delete=models.CASCADE)







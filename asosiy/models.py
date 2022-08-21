from django.db import models
from userapp.models import Profil
class Post(models.Model):
    matn=models.TextField()
    vaqt=models.DateTimeField(auto_now_add=True)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    def __str__(self):
        return self.profil

class Efir(models.Model):
    matn = models.TextField()
    koryapturganlar_soni=models.PositiveIntegerField()
    boshlangan_vaqti=models.TimeField(auto_now_add=True)
    profil=models.OneToOneField(Profil,on_delete=models.CASCADE)

class Media(models.Model):
    video=models.URLField()
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

class Like(models.Model):
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    class Meta:
        unique_together=[["profil","post_id"]]

class Comment(models.Model):
    matn=models.CharField(max_length=500)
    sana=models.DateField(auto_now_add=True)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)

class Comment_like(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    class Meta:
        unique_together=[["comment","profil"]]


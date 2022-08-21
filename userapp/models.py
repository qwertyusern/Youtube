from django.contrib.auth.models import User
from django.db import models
class Profil(models.Model):
    username=models.CharField(max_length=120)
    rasm=models.URLField(blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Connection(models.Model):
    follower=models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="follower")
    following=models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="following")


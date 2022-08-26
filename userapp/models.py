from django.contrib.auth.models import User
from django.db import models

class Kanal(models.Model):
    nomi=models.CharField(max_length=20)
    rasm=models.FileField()
    follower=models.PositiveIntegerField()
    following=models.PositiveIntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)



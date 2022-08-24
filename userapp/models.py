from django.contrib.auth.models import User
from django.db import models
class Account(models.Model):
    username=models.CharField(max_length=120)
    rasm=models.URLField(blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)


class Connection(models.Model):
    follower=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="follower")
    following=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="following")



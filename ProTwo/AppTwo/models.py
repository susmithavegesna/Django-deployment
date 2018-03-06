from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usertab(models.Model):
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)
    Email = models.EmailField(max_length=264,unique=True)

    def __str__(self):
        return self.FirstName

class userprofileinfotab(models.Model):
    user = models.OneToOneField(User)

    #additional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username

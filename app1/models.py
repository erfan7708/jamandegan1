from django.db import models
#from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# class Profile(models.Model):
#     username = models.OneToOneField(User , on_delete=models.CASCADE)
#     bio = models.CharField(max_length=100)
#     gender = (
#         ('F' , 'Female'),
#         ('M' , 'Male'),
#         ('O' , 'Other'),
#     )
# @receiver(post_save , sender=User)
# def create_user_profile(sender ,instance,created,**kwargs ):
#     if created:
#         Profile.objects.create(username=sender)
# @receiver(post_save , sender=Profile)
# def save_user_profile(sender , instance , **kwargs):
#     instance.profile.save()

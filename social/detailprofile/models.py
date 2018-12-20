from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    designation = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=200, default='')
    website = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=10, default='')
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
          ProfileUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profileuser.save()

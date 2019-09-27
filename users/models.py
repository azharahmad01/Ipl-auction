from django.contrib.auth.models import User,AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
	is_owner = models.BooleanField(default=False)
	is_player = models.BooleanField(default=False)
	image = models.ImageField(default = 'default.jpg',upload_to = 'profile_pics')

class Player(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='user_player')
	base_price = models.CharField(max_length=100)
	
class Owner(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='user_owner')
	team_name = models.CharField(max_length=100)
	
	
  


	


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	
	if instance.is_player:
		Player.objects.get_or_create(user = instance)
	elif instance.is_owner:
		Owner.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created,**kwargs):
	
	if instance.is_player:
		instance.user_player.save()
	elif instance.is_owner:
		instance.user_owner.save()
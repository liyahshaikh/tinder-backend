from django.db import models

# Create your models here.
class Profile(models.Model):
	userName=models.CharField(max_length=120)
	userBio=models.TextField(blank=True, null=True)
	userAge=models.IntegerField()

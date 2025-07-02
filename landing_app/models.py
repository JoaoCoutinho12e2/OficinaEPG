from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    user_image = models.ImageField(null=True, blank=True)
    first_name = models.CharField(verbose_name="First name", max_length=50)
    last_name = models.CharField(verbose_name="Last Name", max_length=50)
    address = models.CharField(verbose_name="Address", max_length=50)
    skills = models.CharField(verbose_name="Skills", max_length=50)
    phone = models.CharField(verbose_name="Phone", max_length=50)
    email = models.CharField(verbose_name="Email", max_length=50)
    aboutme = models.CharField(verbose_name="About me", max_length=500)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    

class skills(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=50)
    percentagem = models.IntegerField(verbose_name="Percentagem", default=1, validators= [MinValueValidor(1), MaxValueValidor(100)])
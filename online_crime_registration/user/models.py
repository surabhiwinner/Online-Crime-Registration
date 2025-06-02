from django.db import models

# Create your models here.

from crimes.models import BaseClass

class User(BaseClass):

    profile = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE)

    name = models.CharField(max_length=70)

    adddress = models.TextField(blank=True, null= True)

    image = models.ImageField(upload_to='user-images/')

    email = models.EmailField(max_length=100)

    # phone_number = models.CharField(max_length=10, unique=True)


    def __str__(self):
        return f'{self.profile}'
    

    class Meta:

        verbose_name = 'User'

        verbose_name_plural = 'User'
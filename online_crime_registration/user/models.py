from django.db import models

# Create your models here.

from crimes.models import BaseClass

class User(BaseClass):

    profile = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='user-images/')

    email = models.EmailField(max_length=100)

    # phone_number = models.IntegerField()


    def __str__(self):
        return f'{self.name}'
    

    class Meta:

        verbose_name = 'User'

        verbose_name_plural = 'User'
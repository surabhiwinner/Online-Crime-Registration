from django.db import models

from crimes.models import BaseClass


class Officers(BaseClass):


    # police_officer = models.CharField(max_length=50)

    police_officer = models.OneToOneField('authentication.Profile',
                                          on_delete=models.SET_DEFAULT,
                                          default=1)

    image = models.ImageField(upload_to='police-officer-images/')

    description = models.TextField()

    def __str__(self):
        return str(self.police_officer)
    
    class Meta:

        verbose_name = 'Officers'

        verbose_name_plural = 'Officers'
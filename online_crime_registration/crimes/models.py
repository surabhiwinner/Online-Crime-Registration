
from django.db import models

import uuid

# Create your models here.
class StatusChoice(models.TextChoices):

    pending = 'Pending','Pending'

    approved = 'Approved', 'Approved'

    rejected = 'Rejected', 'Rejected'


class CategoryChoice(models.TextChoices):

    crimes_against_persons =  'Crimes Against Persons', ' Crimes Against Persons'

    crimes_against_property = 'Crimes Against Property', 'Crimes Against Property'

    white_collar_crimes  = ' White-Collar Crimes', ' White-Collar Crimes'
     
    crimes_against_society = ' Crimes Against Society',' Crimes Against Society'
     
    cybercrimes = ' Cybercrimes', ' Cybercrimes'


class BaseClass(models.Model):

    uuid = models.SlugField(
                            default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta :

        abstract = True

class Crimes(BaseClass):

    reporting_user = models.CharField(max_length=50)

    title = models.CharField(max_length=100)
    
    reporting_date = models.DateField()

    category = models.CharField(max_length=25,choices=CategoryChoice.choices)

    status = models.CharField(max_length=50,choices = StatusChoice.choices)

    police_officer = models.ForeignKey('police_officers.Officers', on_delete=models.SET_DEFAULT,
                                       default=1)


    def __str__(self):
        return f'{self.category}--{self.title}--{self.police_officer}'
    
    class Meta :

        verbose_name = 'Crimes'

        verbose_name_plural = 'Crimes'

        ordering = ['id']

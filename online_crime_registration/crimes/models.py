
from django.db import models

import uuid




# Create your models here.
class StatusChoice(models.TextChoices):

    PENDING = 'Pending','Pending'

    APPROVED = 'Approved', 'Approved'

    REJECTED = 'Rejected', 'Rejected'


class CategoryChoice(models.TextChoices):

    CRIMES_AGAINST_PERSONS =  'Crimes Against Persons', ' Crimes Against Persons'

    CRIMES_AGAINST_PROPERTY = 'Crimes Against Property', 'Crimes Against Property'

    WHITE_COLLAR_CRIMES  = ' White-Collar Crimes', ' White-Collar Crimes'
     
    CRIMES_AGAINST_SOCIETY = ' Crimes Against Society',' Crimes Against Society'
     
    CYBERCRIMES = ' Cybercrimes', ' Cybercrimes'


class BaseClass(models.Model):

    uuid = models.SlugField(
                            default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta :

        abstract = True

class Crimes(BaseClass):

    reporting_user = models.ForeignKey('user.User',on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    
    reporting_date = models.DateField()

    category = models.CharField(max_length=25,choices=CategoryChoice.choices)

    status = models.CharField(max_length=50,choices = StatusChoice.choices,default=StatusChoice.PENDING)

    police_officer = models.ForeignKey('police_officers.Officers', on_delete=models.SET_NULL, null=True,blank=True)


    def __str__(self):
        return f'{self.category}--{self.title}--{self.police_officer or 'No officer assigned'}'
    
    class Meta :

        verbose_name = 'Crimes'

        verbose_name_plural = 'Crimes'

        ordering = ['id']

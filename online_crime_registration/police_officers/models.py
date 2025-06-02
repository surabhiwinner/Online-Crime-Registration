from django.db import models

from crimes.models import BaseClass

class RankOfOfficer(BaseClass):

    rank = models.CharField(max_length=50)

    def __str__(self):

        return self.rank
    
    class Meta:

        verbose_name = 'Rank of Officers'

        verbose_name_plural = 'Rank of Officers'

class Officers(BaseClass):


    # police_officer = models.CharField(max_length=50)

    profile = models.OneToOneField('authentication.Profile',
                                          on_delete=models.CASCADE)
    police_officer = models.CharField(max_length=50)

    image = models.ImageField(upload_to='police-officer-images/')

    description = models.TextField()

    rank_of_officer = models.ForeignKey('RankOfOfficer',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.police_officer)
    
    class Meta:

        verbose_name = 'Officers'

        verbose_name_plural = 'Officers'
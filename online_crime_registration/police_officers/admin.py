from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Officers)
admin.site.register(models.RankOfOfficer)

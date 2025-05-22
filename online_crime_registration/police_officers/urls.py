from django.urls import path

from . import views

from .models import Officers

urlpatterns = [
    path('officers-list/', views.OfficerListView.as_view(), name= 'officers-list'),
    path('add-new-officer/',views.AddNewPoliceOfficersView.as_view(), name ='add-new-officer')
]
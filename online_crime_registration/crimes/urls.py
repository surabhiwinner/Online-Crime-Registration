from django.urls import path

from . import views

urlpatterns = [

    path('crimes-list/',views.CrimesListView.as_view(),name='crimes'),
    
    path('contact-page/', views.ContactView.as_view(),name='contact'),
    path('about-page/', views.AboutView.as_view(), name='about'),
    path('update-crime/<str:uuid>/', views.CrimeUpdateView.as_view(), name='crime-update'),
    path('report-crime/', views.ReportCrimeView.as_view(), name='report-crime'),
    path('crime-details/<str:uuid>/', views.CrimeDetailsView.as_view(), name= 'crime-details'),
    path('crime-delete/<str:uuid>/', views.CrimeDeleteView.as_view(), name='crime-delete')

]


























"""
URL configuration for online_crime_registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crimes import views


from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crimes/',include('crimes.urls')),
    path('officers/',include('police_officers.urls')),
    path('authentication', include('authentication.urls')),
    path('user/', include('user.urls')),
    path('',views.HomeView.as_view(),name= 'home'),
]


urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
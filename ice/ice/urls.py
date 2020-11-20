"""ice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import handler400, handler403, handler404, handler500
from ams import views as ams_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', ams_views.dashboard),
    path('ams/', include('ams.urls')),
]

handler400 = 'ice.views.handler400'
handler403 = 'ice.views.handler403'
handler404 = 'ice.views.handler404'
handler500 = 'ice.views.handler500'

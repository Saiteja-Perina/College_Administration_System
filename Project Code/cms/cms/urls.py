"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',center,name='center'),
    path('faclog/',faclog,name='faclog'),
    path('studlog/',studlog,name='studlog'),
    path('feecheck/<str:id>',feecheck,name='feecheck'),
    path('choose/<str:id>',choose,name='choose'),
    path('choose1/<str:id>',choose1,name='choose1'),
    path('markattend/<str:id>',markattend,name='markattend'),
    path('entermarks/<str:id>',entermarks,name='entermarks'),
    path('attendancecheck/<str:id>',attendancecheck,name='attendancecheck'),
    path('markscheck/<str:id>',markscheck,name='markscheck'),
]
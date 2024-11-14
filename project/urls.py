"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),# syntax of an include path is: `appname.filename`
    path('timers/', include('timers.urls')),
    path('habit_helpers/', include('habit_helpers.urls')),
    path('journals/', include('journals.urls')),
    path('awards/', include('awards.urls')),
    path('completed_habit_helpers/', include('completed_habit_helpers.urls')),
    path('quotes/', include('quotes.urls')),
]

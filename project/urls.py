
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

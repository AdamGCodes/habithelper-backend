from django.urls import path
from .views import ListCreateTimerView, RetrieveUpdateDestroyTimerView

#Remember all of these are prefixed with /timers/
urlpatterns = [
    path('', ListCreateTimerView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyTimerView.as_view())
]

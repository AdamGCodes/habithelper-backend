from django.urls import path
from .views import ListCreateAwardView, RetrieveUpdateDestroyAwardView

# Remember all of these are prefixed with /timers/
urlpatterns = [
    path('', ListCreateAwardView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyAwardView.as_view())
]

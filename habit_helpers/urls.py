from django.urls import path
from .views import ListCreateHabit_HelperView, RetrieveUpdateDestroyHabit_HelperView

# Remember all of these are prefixed with /timers/
urlpatterns = [
    path('', ListCreateHabit_HelperView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyHabit_HelperView.as_view())
]

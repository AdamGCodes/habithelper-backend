from django.urls import path
from .views import ListCreateCompleted_Habit_HelperView, RetrieveUpdateDestroyCompleted_Habit_HelperView

# Remember all of these are prefixed with /timers/
urlpatterns = [
    path('', ListCreateCompleted_Habit_HelperView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyCompleted_Habit_HelperView.as_view())
]

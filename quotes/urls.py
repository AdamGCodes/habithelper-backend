from django.urls import path
from .views import ListCreateQuoteView, RetrieveUpdateDestroyQuoteView

# Remember all of these are prefixed with /timers/
urlpatterns = [
    path('', ListCreateQuoteView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyQuoteView.as_view())
]

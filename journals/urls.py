from django.urls import path
from .views import ListCreateJournalView, RetrieveUpdateDestroyJournalView

# Remember all of these are prefixed with /journals/
urlpatterns = [
    path('', ListCreateJournalView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyJournalView.as_view())
]

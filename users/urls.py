from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignUpView, SignInView


urlpatterns = [
    # /users/signup
    path('signup/', SignUpView.as_view()), 
    # /users/signin
    path('signin/', SignInView.as_view())
]
# path('signin/', TokenObtainPairView.as_view())

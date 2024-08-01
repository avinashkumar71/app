from django.urls import path
from .views import UserRegistrationViews,UserLoginView,UserProfileView

urlpatterns = [
    path('register/',UserRegistrationViews.as_view()),
    path('login/',UserLoginView.as_view()),
    path('profile/',UserProfileView.as_view())
]
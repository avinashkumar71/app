from django.urls import path
from .views import CategoryApiView
urlpatterns = [
    path('', CategoryApiView.as_view()),
]
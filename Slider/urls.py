from django.urls import path
from .views import SliderCarouselApiView
urlpatterns = [
    path('carousel/', SliderCarouselApiView.as_view()),
]
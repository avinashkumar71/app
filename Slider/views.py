from .models import CarouselModel,CarouselSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class SliderCarouselApiView(APIView):
    def get(self,pk=None):
        images = CarouselModel.objects.all()
        serializer = CarouselSerializer(images,many=True)
        return Response(serializer.data)



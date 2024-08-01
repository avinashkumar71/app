from .models import ProductsModel
from .serializer import ProductsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class ProductApiView(APIView):
    def get(self,pk=None):
        category_items  = ProductsModel.objects.all()
        serializer = ProductsSerializer(category_items,many=True)
        return Response(serializer.data)

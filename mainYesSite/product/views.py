from django.db.models import Q
from django.http import Http404

from .serializers import ProductSerialiser, CategorySerializer
from .models import Category, Product

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerialiser(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerialiser(product)
        return Response(serializer.data)
    
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if(query):
        products = Product.objects.filter(Q(name__incontains=query | Q(description__icontains=query)))
        serializer = ProductSerialiser(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
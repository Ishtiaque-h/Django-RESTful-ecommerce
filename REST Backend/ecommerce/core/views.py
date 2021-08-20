from django.http.response import JsonResponse
from .models import Product, ProductType
from .serializers import ProductTypeSerializer, ProductViewSerializer, ProductDetailsSerializer
from rest_framework.views import APIView
from rest_framework import status, permissions


# Create your views here.
class HomeView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request): 

        products = Product.objects.order_by('-id')[:12]
        products = ProductViewSerializer(products, many=True)

        data= {
            #'product_types':product_types.data,
            'products': products.data,
        }
        return JsonResponse(data) 

class ProductTypesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        product_types = ProductType.objects.order_by('title')
        product_types = ProductTypeSerializer(product_types, many=True)

        data= {
            'product_types': product_types.data,
        }
        return JsonResponse(data)

class ProductDetailsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, product_id):
        product_details = Product.objects.get(pk=product_id)
        product_details = ProductDetailsSerializer(product_details, many=True)

        data= {
            'product_details': product_details.data,
        }
        return JsonResponse(data)
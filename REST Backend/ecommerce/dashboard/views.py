from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser
from django.contrib.auth.models import User
from core.models import ProductType, Product
from core.serializers import ProductTypeSerializer, ProductSerializer
from django.http import JsonResponse

# Create your views here.
class Dashboard(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        total_users = User.objects.count()
        product_types = ProductType.objects.count()
        products = Product.objects.count()
        data={
            'total_users': total_users,
            'product_types' : product_types,
            'products': products
        }
        return JsonResponse(data)

class ProductTypeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        product_types = ProductType.objects.order_by('-id')
        product_types = ProductTypeSerializer(product_types, many=True) 
        #To serialize a queryset or list of objects instead of a single object instance, you should pass the many=True
        return JsonResponse({'product_types': product_types.data})


    def post(self, request):
        title= request.data["title"]
        if ProductType.objects.filter(title__iexact=title).exists():
            return JsonResponse({'status':10})
        product_type = ProductType(title=title)
        product_type.save()
        return JsonResponse({'status':1, 'id':product_type.pk})
    

    def put(self, request):
        try:
            _id= request.data["_id"]
            title= request.data["title"]
            if ProductType.objects.filter(title__iexact=title).exclude(pk=_id).exists():
                return JsonResponse({'status':10})
            product_type = ProductType.objects.get(pk=_id)
            product_type.title = title
            product_type.save()
            return JsonResponse({'status':1})
        except:
            return JsonResponse({'status':2})
    
        
    def delete(self, request):
        try:
            _id= request.data["_id"]
            product_type = ProductType.objects.get(pk=_id)
            product_type.delete()
            return JsonResponse({'status':1})
        except:
            return JsonResponse({'status':2})
    
class ProductView(APIView):
    permission_class = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, )

    def get(self, request):
        product_types = ProductType.objects.order_by('-id')
        product_types = ProductTypeSerializer(product_types, many=True)

        products = Product.objects.order_by('-id')
        products = ProductSerializer(products,many=True)

        data= {
            'product_types':product_types.data,
            'products': products.data
        }
        return JsonResponse(data)
       
    def post(self, request):

        product_serializer = ProductSerializer(data = request.data)
        title = request.data['title']
        #print(request.data['product_type'])
        #print(product_serializer)
        if product_serializer.is_valid():
            if Product.objects.filter(title__iexact=title).exists():
                return JsonResponse({'status':1})
            product_serializer.save()
            return JsonResponse({'status':2})
        #print(str(product_serializer.errors))
        return JsonResponse({'status':3, 'the_error': str(product_serializer.errors)})
    
    def put(self, request):
        pass

class UpdateProductView(APIView):
    permission_class = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, )

    def get(self, request, product_id):
        #print(product_id)
        product_types = ProductType.objects.order_by('-id')
        product_types = ProductTypeSerializer(product_types, many=True)

        product = Product.objects.get(pk=product_id)
        product = ProductSerializer(product)

        data= {
            'product_types':product_types.data,
            'product': product.data
        }
        return JsonResponse(data)

    def put(self, request, product_id):
        try:
            title = request.data['title']
            if Product.objects.filter(title__iexact=title).exclude(pk=product_id).exists():
                return JsonResponse({'status':1})
            product = Product.objects.get(pk=product_id)
            the_image = product.image
            product_serializer=ProductSerializer(product, data=request.data, partial=True)
            if product_serializer.is_valid():                
                product_serializer.save()
                if not 'image' in request.data:
                    product.image = the_image
                    product.save()
                return JsonResponse({'status':2})
            print(product_serializer.errors)
            return JsonResponse({'status':3, 'the_error': str(product_serializer.errors)})
        except Exception as e:
            print(e)
            return JsonResponse({'status':3})



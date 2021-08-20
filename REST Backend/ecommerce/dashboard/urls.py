from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard' ),
    path('product-types', views.ProductTypeView.as_view(), name='product-types' ),
    path('products', views.ProductView.as_view(), name='products' ),
    path('update-product/<int:product_id>', views.UpdateProductView.as_view(), name='update-product'),
]

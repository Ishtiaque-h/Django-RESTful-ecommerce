from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.HomeView.as_view(), name='home' ),
    path('product-types', views.ProductTypesView.as_view(), name='product-types' ),
    path('product-details/<int:product_id>', views.ProductDetailsView.as_view(), name='product-details' ),
]

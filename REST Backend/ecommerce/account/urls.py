from . import views
from django.urls import path,include

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup' ),
    path('login',views.LogIn.as_view(), name='login'),
]

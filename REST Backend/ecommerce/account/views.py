#from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import JsonResponse, request


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class SignUp(APIView):
    
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        #print(request.user)
        name = request.data['name']
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        if User.objects.filter(username__iexact = username ).exists():       
            return JsonResponse({'status': 1})           
        
        if User.objects.filter(email__iexact = email ).exists():
            return JsonResponse({'status': 2})
        user = User.objects.create_user(first_name=name,email=email,username=username,password=password)
        user.save()
        token = get_tokens_for_user(user)
        return JsonResponse({'status':3,'token':token})


#permission_classes = (permissions.IsAuthenticated,)


class LogIn(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get('username',"")
        password = request.data['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            token = get_tokens_for_user(user)
            #messages.success(request, 'You are succsssfully logged in')
            #return redirect('', user)
            return JsonResponse({'status':1, 'token':token})
        return JsonResponse({'status':2})
        #if request.user.is_authenticated():
            #messages.success(request, 'You are already logged in')
            #return JsonResponse({'status':3})
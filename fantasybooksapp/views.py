from django.shortcuts import render
from rest_framework import generics, status
from .models import *
from .serializers import *
# Auth
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from knox.models import AuthToken
from django.contrib.auth import authenticate

########## User ##########################################################
class RegisterViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUserSerializer

    def create(self, request):
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class LoginViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def create(self, request):
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, email=email, password=password) #This is refering to auth_backend.py and checks email and password
            if user:
                _, token = AuthToken.objects.create(user) # This creates a tupple with 1st possition empty(_,) and second a token for the user
                return Response(
                    {
                        'user': self.serializer_class(user).data,
                        'token': token,
                        'userId':user.id,
                    }
                )
            else:
                return Response({'error':'Invalid user credentials'}, status=401)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUserSerializer

    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer= self.serializer_class(queryset, many = True)
        
        return Response(serializer.data)
    

########## Bookmark ##################################################################
class BookmarkListCreateView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookmarkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

########## Book Description ##########################################################
class BookDescriptionListCreateView(generics.ListCreateAPIView):
    queryset = Book_Description.objects.all()
    serializer_class = BookDescriptionSerializer

class BookDescriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book_Description.objects.all()
    serializer_class = BookDescriptionSerializer
    
########## Book ######################################################################
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

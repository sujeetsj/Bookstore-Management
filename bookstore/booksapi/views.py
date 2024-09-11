from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated]

    def get_permission(self):
        if self.action['list','retrive']:
            return []
        return [permission() for permission in self.permission_classes]
    
# api/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

def index(request):
    return render(request, 'index.html')
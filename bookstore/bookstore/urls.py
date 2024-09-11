# bookstore/urls.py
from django.contrib import admin
from django.urls import path, include
from booksapi.views import index  # Adjust the import according to your app structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('booksapi.urls')), 
    path('', index, name='index'),  # Home page routes to the index view
 # Include the API URLs from the api app
]


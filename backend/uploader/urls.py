# backend/urls.py
from django.urls import path
from . import views  # Adjust the import based on your project structure

urlpatterns = [
    path('', views.upload_file, name='upload_file'),  # Your existing upload URL
    path('download/', views.download_summary, name='download_summary'),  # Ensure this is correct
    path('about/', views.about, name='about'),  # Your existing upload URL
]

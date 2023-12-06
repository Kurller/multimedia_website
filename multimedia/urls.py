# multimedia/urls.py
from django.urls import path
from .views import image_list, upload_image

urlpatterns = [
    path('', image_list, name='image_list'),
    path('upload/', upload_image, name='upload_image'),
]

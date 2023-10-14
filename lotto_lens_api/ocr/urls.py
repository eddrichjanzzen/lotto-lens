from django.urls import path
from .views import ocr_endpoint

urlpatterns = [
    path('process_ocr/', ocr_endpoint, name='process_ocr'),
]
# urls.py
from django.urls import path
from .views import ExcelUploadView

urlpatterns = [
    path('api/upload/', ExcelUploadView.as_view(), name='excel-upload'),
]

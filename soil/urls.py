from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.soil_upload_view, name='soil_upload'),
    path('result/<int:image_id>/', views.soil_result_view, name='soil_result'),
]

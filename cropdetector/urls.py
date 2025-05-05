from django.urls import path
from . import views


urlpatterns=[
    path('upload/',views.upload_crop_image,name='crop_image'),

]

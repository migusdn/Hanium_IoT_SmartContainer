from django.urls import path
from . import views

urlpatterns = [
    path('<device_num>', views.device, name='device'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<file_name>',views.download,name='download')
]

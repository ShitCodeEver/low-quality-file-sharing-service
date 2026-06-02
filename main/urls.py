from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='Home'),
    path('create/', views.NewView.as_view(), name='Create')
]
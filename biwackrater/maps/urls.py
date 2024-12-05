from . import views
from django.urls import path

urlpatterns = [
    path('', views.MapView.init_maps),
]

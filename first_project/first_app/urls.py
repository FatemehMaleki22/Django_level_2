from first_app import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('user',views.user),
    path('signup', views.signup),
]

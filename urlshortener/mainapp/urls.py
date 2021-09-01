from django.urls import path
from . import views

urlpatterns = [
    path('urls/', views.show_all, name='show-all'),
    # path('about/', views.about, name="memes-about"),
    path('go/<str:url>/', views.show, name='show-url'),
    path('', views.create, name='create-url')
]
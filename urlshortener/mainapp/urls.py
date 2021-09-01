from django.urls import path
from . import views

urlpatterns = [
    path('url/', views.show_recent, name='show-recent'),
    # path('about/', views.about, name="memes-about"),
    path('go/<str:url>/', views.show, name='show-url'),
    path('', views.create, name='create-url')
]
from django.urls import path
from . import views
urlpatterns = [
    path('new/', views.new, name='new'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
]
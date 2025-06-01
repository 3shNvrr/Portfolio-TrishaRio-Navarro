from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('favorites/', views.favorites, name='favorites'),
    path('contact/', views.contact, name='contact'),
    path('meow/', views.secret, name='meow'),
]

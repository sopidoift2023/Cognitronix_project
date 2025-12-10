from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('faq/', views.faq, name='faq'),
    path('join/', views.join, name='join'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
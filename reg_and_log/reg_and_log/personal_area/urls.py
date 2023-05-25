from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('succsessfully/', views.suc, name='succsessfully'),
    path('error/', views.error, name='error'),

]

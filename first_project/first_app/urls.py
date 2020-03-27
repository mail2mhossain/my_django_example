from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('index', views.index, name='index'),
    path('logout', views.user_logout, name='logout'),
    path('newWebpage', views.newWebpage, name='newWebpage'),
    path('register', views.register, name='register'),
]

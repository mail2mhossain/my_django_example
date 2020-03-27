from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
    path('newAuthor', views.NewAuthor, name='newAuthor'),
    path('newBook', views.NewBook, name='newBook'),
]

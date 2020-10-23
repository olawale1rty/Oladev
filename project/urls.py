from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from project import views

app_name = 'project'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:project_id>', views.detail, name='detail'),
    path('new_client/', views.Client.as_view(), name = 'new_client')

]
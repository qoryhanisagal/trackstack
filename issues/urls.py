from django.urls import path
from . import views

app_name = 'issues'

urlpatterns = [
    path('', views.issue_board, name='list'),
    path('create/', views.issue_create, name='create'),
]
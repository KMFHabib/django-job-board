from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
]

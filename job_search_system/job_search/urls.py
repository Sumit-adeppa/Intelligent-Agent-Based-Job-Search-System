from django.urls import path
# from .views import register
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('job_list/', views.job_list, name='job_list'),
]

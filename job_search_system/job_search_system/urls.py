"""
URL configuration for job_search_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Root view redirect
def home(request):
    return redirect('upload_resume')  # You can change this to any page you want as the home page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job_search/', include('job_search.urls')),
    path('', home),  # Redirect root URL to the home view (job_search)
]


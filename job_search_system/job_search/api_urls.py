from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    CareerPortalViewSet, 
    JobViewSet, 
    ResumeViewSet, 
    ResumeUploadAPIView,
    JobListAPIView
)

# Using DefaultRouter for automatic URL routing for ViewSets
router = DefaultRouter()
router.register(r'portals', CareerPortalViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'resumes', ResumeViewSet)

urlpatterns = [
    # Include all router-generated URLs
    path('', include(router.urls)),
    
    # Custom API endpoints
    path('upload-resume/', ResumeUploadAPIView.as_view(), name='api_upload_resume'),
    path('internal-jobs/', JobListAPIView.as_view(), name='api_job_list'),
]

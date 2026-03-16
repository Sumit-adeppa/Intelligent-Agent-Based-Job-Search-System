from rest_framework import serializers
from .models import CareerPortal, Job, Resume

class CareerPortalSerializer(serializers.ModelSerializer):
    """
    Serializer for the CareerPortal model.
    Handles the conversion of CareerPortal objects to JSON and vice versa.
    """
    class Meta:
        model = CareerPortal
        fields = ['id', 'company_name', 'portal_url']

class JobSerializer(serializers.ModelSerializer):
    """
    Serializer for the Job model.
    Used for exposing available jobs via the REST API.
    """
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'required_skills']

class ResumeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Resume model.
    Handles resume file uploads and skill storage.
    """
    class Meta:
        model = Resume
        fields = ['id', 'user_name', 'uploaded_file', 'extracted_skills']
        read_only_fields = ['extracted_skills']

class JobRecommendationSerializer(serializers.Serializer):
    """
    Custom Serializer for job recommendations.
    This is not tied to a specific model but represents the structure
     of a matched job result from the Excel data.
    """
    job_role = serializers.CharField()
    company_name = serializers.CharField()
    matched_skills = serializers.ListField(child=serializers.CharField())
    match_percentage = serializers.FloatField()
    Job_details_link = serializers.CharField()
    apply_link = serializers.CharField()

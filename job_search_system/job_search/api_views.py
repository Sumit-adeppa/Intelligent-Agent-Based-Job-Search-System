from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import CareerPortal, Job, Resume
from .serializers import (
    CareerPortalSerializer, 
    JobSerializer, 
    ResumeSerializer, 
    JobRecommendationSerializer
)
from .views import load_jobs_from_excel, parse_skills, match_jobs
from pypdf import PdfReader
import io

class CareerPortalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Career Portals to be viewed or edited.
    """
    queryset = CareerPortal.objects.all()
    serializer_class = CareerPortalSerializer

class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Jobs to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Resumes to be viewed or edited.
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeUploadAPIView(APIView):
    """
    API endpoint for uploading a resume and getting job recommendations.
    Accepts a PDF file and returns matching jobs from the internal data source.
    """
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        user_name = request.data.get('user_name', 'Anonymous')
        resume_file = request.FILES.get('resume_file')

        if not resume_file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        if not resume_file.name.endswith('.pdf'):
            return Response({"error": "Invalid file type. Please upload a PDF file."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Read PDF content
            reader = PdfReader(resume_file)
            full_text = []

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text.append(text)

            resume_text = "\n\n".join(full_text)
            
            # Extract skills using the existing logic in views.py
            skills = parse_skills(resume_text)
            
            if not skills:
                return Response({"error": "No skills could be extracted from your resume."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            # Load job data and match
            job_data = load_jobs_from_excel()
            if job_data is None:
                return Response({"error": "Failed to load job data from the internal source."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            recommendations = match_jobs(skills, job_data)

            # Optional: Save resume record to database
            resume_instance = Resume.objects.create(
                user_name=user_name,
                uploaded_file=resume_file,
                extracted_skills=", ".join(skills)
            )

            # Serialize recommendations
            serializer = JobRecommendationSerializer(recommendations, many=True)

            return Response({
                "user_name": user_name,
                "resume_id": resume_instance.id,
                "extracted_skills": skills,
                "recommendations": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class JobListAPIView(APIView):
    """
    API endpoint to list all jobs from the internal Excel data source.
    """
    def get(self, request, *args, **kwargs):
        job_data = load_jobs_from_excel()

        if job_data is None:
            return Response({"error": "Failed to load job data."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        recommendations = []
        for _, row in job_data.iterrows():
            recommendations.append({
                'company_name': row.get('Company Name', 'N/A'),
                'job_role': row.get('Job Role', 'N/A'),
                'Job_details_link': row.get('Job URL', '#'),
                'apply_link': row.get('Apply URL', '#'),
                'match_percentage': 0,
                'matched_skills': []
            })
        
        serializer = JobRecommendationSerializer(recommendations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

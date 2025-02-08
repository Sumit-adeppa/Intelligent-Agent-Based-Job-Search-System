from django.db import models

class CareerPortal(models.Model):
    company_name = models.CharField(max_length=100)  # Name of the company
    portal_url = models.URLField()  # URL of the career portal

    def __str__(self):
        return self.company_name


class Job(models.Model):
    title = models.CharField(max_length=200)  # Job title
    experiece = models.IntegerField(0) # Experience
    description = models.TextField()  # Job description
    required_skills = models.TextField()  # Skills required for the job

    def __str__(self):
        return self.title


class Resume(models.Model):
    user_name = models.CharField(max_length=100)  # Name of the user uploading the resume
    uploaded_file = models.FileField(upload_to='resumes/')  # The uploaded resume file (PDF, DOCX, etc.)
    extracted_skills = models.TextField(blank=True, null=True)  # Skills extracted from the resume

    def __str__(self):
        return self.user_name

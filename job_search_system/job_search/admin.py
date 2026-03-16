from django.contrib import admin
from .models import CareerPortal, Job, Resume

@admin.register(CareerPortal)
class CareerPortalAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'portal_url')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'required_skills')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'uploaded_file')

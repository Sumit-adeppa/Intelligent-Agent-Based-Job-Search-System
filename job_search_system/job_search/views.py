
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.conf import settings
from .forms import ResumeUploadForm
from .models import Job
import pandas as pd
import spacy
import json
import os
from datetime import datetime
from rapidfuzz import process, fuzz
from pypdf import PdfReader
from django.core.exceptions import ValidationError

# Load spaCy model once for better performance
try:
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    print(f"Error loading spaCy model: {e}")
    nlp = None

def get_job_data_path():
    return os.path.join(settings.BASE_DIR, "job_search", "data", "job_data.xlsx")

def get_skills_db_path():
    return os.path.join(settings.BASE_DIR, "scripts", "skills_db.json")

def load_jobs_from_excel():
    file_path = get_job_data_path()
    try:
        if not os.path.exists(file_path):
            print(f"Excel file not found at: {file_path}")
            return None
        job_data = pd.read_excel(file_path)
        return job_data
    except Exception as e:
        print(f"Error loading Excel file: {str(e)}")
        return None

def parse_skills(resume_text):
    if nlp:
        doc = nlp(resume_text)
        # You could use spaCy labels here if needed
        # For now, keeping the original logic but optimized
    
    skills_path = get_skills_db_path()
    try:
        with open(skills_path, "r") as file:
            SKILLS_DB = json.load(file)
    except Exception as e:
        print(f"Error loading skills database: {e}")
        return []

    extracted_skills = set()
    words = resume_text.split()

    for word in words:
        # Extract matches for each "word" isn't the best way for multi-word skills, 
        # but matching requirements given by current implementation.
        matches = process.extract(word, SKILLS_DB, scorer=fuzz.ratio, limit=2)
        for match in matches:
            skill, score, _ = match
            if score > 80:
                extracted_skills.add(skill)
    return sorted(list(extracted_skills))

def match_jobs(resume_skills, job_data):
    recommendations = []
    resume_skills_lower = [skill.lower() for skill in resume_skills]
    
    for _, row in job_data.iterrows():
        job_description = str(row.get('Job Description', '')).lower()
        job_role = row.get('Job Role', 'N/A')
        company_name = row.get('Company Name', 'N/A')
        job_link = row.get('Job URL', '#')
        apply_link = row.get('Apply URL', '#')
        
        matched_skills = [skill for skill in resume_skills if skill.lower() in job_description]
        if matched_skills:
            match_percentage = (len(matched_skills) / len(resume_skills)) * 100
            recommendations.append({
                'job_role': job_role,
                'company_name': company_name,
                'matched_skills': matched_skills,
                'match_percentage': round(match_percentage, 2), # Keep as float for sorting and template formatting
                'Job_details_link': job_link,
                'apply_link': apply_link,
            })
    
    recommendations.sort(key=lambda x: x['match_percentage'], reverse=True)
    return recommendations

def upload_resume(request):
    error_message = None
    if request.method == 'POST':
        if 'resume_file' in request.FILES:
            resume_file = request.FILES['resume_file']
            if not resume_file.name.endswith('.pdf'):
                error_message = "Invalid file type. Please upload a PDF file."
            else:
                try:
                    reader = PdfReader(resume_file)
                    full_text = []

                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            full_text.append(text)

                    resume_text = "\n\n".join(full_text)
                    skills = parse_skills(resume_text)
                    
                    if not skills:
                        error_message = "No skills could be extracted from your resume."
                    else:
                        job_data = load_jobs_from_excel()
                        if job_data is None:
                            error_message = "Failed to load job data from the internal Excel file."
                        else:
                            recommendations = match_jobs(skills, job_data)
                            
                            # Pagination
                            paginator = Paginator(recommendations, 10)
                            page_number = request.GET.get('page')
                            page_obj = paginator.get_page(page_number)

                            return render(request, 'job_search/job_list.html', {
                                'recommendations': page_obj,
                                'page_obj': page_obj,
                                'parsed_skills': skills,
                                'current_year': datetime.now().year
                            })

                except Exception as e:
                    error_message = f"An error occurred while processing the file: {str(e)}"
        else:
            error_message = "No file uploaded."
    return render(request, 'job_search/upload_resume.html', {'error_message': error_message})

def job_list(request):
    job_data = load_jobs_from_excel()

    if job_data is None:
        return render(request, 'job_search/job_list.html', {'error': "Failed to load job data."})

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

    # Pagination
    paginator = Paginator(recommendations, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'job_search/job_list.html', {
        'recommendations': page_obj,
        'page_obj': page_obj,
        'current_year': datetime.now().year
    })

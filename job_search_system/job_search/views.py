from django.shortcuts import render
from django.http import HttpResponse
from .forms import ResumeUploadForm
from .models import Job
import pandas as pd
import spacy
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pypdf import PdfReader
from django.core.exceptions import ValidationError
from django.shortcuts import render
JOB_DATA_PATH = "C:/Users/Shree Sai/Desktop/Intelligent-Agent-Based-Job-Search-System/job_search_system/job_search/data/job_data.xlsx"

def load_jobs_from_excel():
    file_path = "C:/Users/Shree Sai/Desktop/Intelligent-Agent-Based-Job-Search-System/job_search_system/job_search/data/job_data.xlsx"
    try:
        job_data = pd.read_excel(file_path)
        return job_data
    except Exception as e:
        print(f"Error loading Excel file: {str(e)}")
        return None


def parse_skills(resume_text):
    nlp = spacy.load("en_core_web_sm")
    with open("C:/Users/Shree Sai/Desktop/Intelligent-Agent-Based-Job-Search-System/job_search_system/scripts/skills_db.json", "r") as file:
        SKILLS_DB = json.load(file)

    extracted_skills = set()
    words = resume_text.split()
    from rapidfuzz import process, fuzz

    for word in words:
        matches = process.extract(word, SKILLS_DB, scorer=fuzz.ratio, limit=2)
        for match in matches:
            skill, score, _ = match
            if score > 80:
                extracted_skills.add(skill)
    return sorted(extracted_skills)

def match_jobs(resume_skills, job_data):
    recommendations = []
    resume_skills = [skill.lower() for skill in resume_skills]
    
    for index, row in job_data.iterrows():
        job_description = row['Job Description'].lower()
        job_role = row['Job Role']
        company_name = row['Company Name']
        job_link = row['Job URL']
        apply_link = row['Apply URL']
        
        matched_skills = [skill for skill in resume_skills if skill in job_description]
        if matched_skills:
            match_percentage = (len(matched_skills) / len(resume_skills)) * 100
            recommendations.append({
                'job_role': job_role,
                'company_name': company_name,
                'matched_skills': matched_skills,
                'match_percentage': f"{match_percentage:.2f}%",
                'Job_details_link': job_link,
                'apply_link': apply_link,

            })
    

    recommendations.sort(key=lambda x: float(x['match_percentage'].replace('%', '')), reverse=True)
    return recommendations

def upload_resume(request):
    error_message = None
    if request.method == 'POST':
        if 'resume_file' in request.FILES:
            resume_file = request.FILES['resume_file']
            if resume_file.content_type != 'application/pdf':
                error_message = "Invalid file type. Please upload a PDF file."
            else:
                try:
                    reader = PdfReader(resume_file)
                    full_text = []

                    for page_num in range(len(reader.pages)):
                        page = reader.pages[page_num]
                        full_text.append(page.extract_text())

                    resume_text = "\n\n".join(full_text)
                    skills = parse_skills(resume_text)
                    job_data = load_jobs_from_excel()
                    if job_data is None:
                        error_message = "Failed to load job data from the internal Excel file."
                    else:
                        recommendations = match_jobs(skills, job_data)

                        return render(request, 'job_search/job_list.html', {
                            'recommendations': recommendations,
                            'parsed_skills': skills,
                        })

                except Exception as e:
                    error_message = f"An error occurred while processing the file: {str(e)}"
        else:
            error_message = "No file uploaded."
    return render(request, 'job_search/upload_resume.html', {'error_message': error_message})

def job_list(request):
    job_data = load_jobs_from_excel()

    if isinstance(job_data, str):
        return render(request, 'job_search/job_list.html', {'error': job_data})

    jobs = []
    for _, row in job_data.iterrows():
        jobs.append({
            'company_name': row.get('Company Name'),
            'job_role': row.get('Job Role'),
            'job_link': row.get('Job Link')
        })

    return render(request, 'job_search/job_list.html', {'jobs': jobs})

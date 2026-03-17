# 🔍 Job Search System

A Django-based web application that intelligently matches job seekers with relevant job opportunities by analyzing uploaded resumes using Natural Language Processing (NLP) and fuzzy skill matching.

---

## 📌 Features

- Resume Upload & Parsing  
  Upload a PDF resume and automatically extract text using pypdf.

- NLP-Based Skill Extraction  
  Uses spaCy along with a curated skills dataset to identify relevant skills from resumes.

- Fuzzy Skill Matching  
  Matches extracted skills with job descriptions using rapidfuzz for better accuracy.

- Smart Job Recommendations  
  Ranks job listings based on how well they match the candidate’s skills.

- Job Listings with Pagination  
  Browse available jobs with clean pagination for better usability.

- Excel-Based Job Data Source  
  Job listings are loaded from an Excel file using pandas.

- Authentication System  
  User registration and login functionality included.

- Django Admin Panel  
  Easily manage jobs, resumes, and related data.

---

## 🛠️ Tech Stack

Backend Framework: Django  
NLP: spaCy (en_core_web_sm)  
Fuzzy Matching: RapidFuzz  
PDF Parsing: pypdf  
Data Processing: pandas, openpyxl  
Database: SQLite3  
Language: Python 3.10+

---

## 📁 Project Structure

job_search_system/
├── job_search/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ ├── admin.py
│ ├── data/
│ │ └── job_data.xlsx
│ ├── templates/
│ │ ├── job_search/
│ │ │ ├── upload_resume.html
│ │ │ ├── job_list.html
│ │ │ ├── post_job.html
│ │ │ └── upload_excel.html
│ │ └── registration/
│ │ ├── login.html
│ │ └── register.html
│ └── migrations/
├── job_search_system/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ ├── wsgi.py
├── scripts/
│ ├── skills_db.json
│ └── excel_sheet_update_standalone.py
├── manage.py
└── db.sqlite3

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

---

### Installation

1. Clone the repository  
git clone https://github.com/your-username/job_search_system.git  
cd job_search_system  

2. Create virtual environment  
python -m venv venv  
source venv/bin/activate      (Windows: venv\Scripts\activate)  

3. Install dependencies  
pip install django spacy rapidfuzz pypdf pandas openpyxl  

4. Download spaCy model  
python -m spacy download en_core_web_sm  

5. Apply migrations  
python manage.py migrate  

6. Run server  
python manage.py runserver  

7. Open in browser  
http://127.0.0.1:8000/  

---

## ⚙️ How It Works

1. User uploads a resume (PDF format)  
2. Text is extracted using pypdf  
3. spaCy processes the text to identify keywords  
4. Skills are matched against a predefined skills database using fuzzy matching  
5. Job descriptions are compared with extracted skills  
6. Jobs are ranked based on match percentage  
7. Results are displayed to the user  

---

## 📊 Data Source

Job data is stored in:  
job_search/data/job_data.xlsx  

Required Columns:

- Job Role  
- Company Name  
- Job Description  
- Job URL  
- Apply URL  

---

## 🗄️ Database Models

- Job — Stores job details and descriptions  
- Resume — Stores uploaded resumes and extracted skills  
- CareerPortal — Stores company portal information  

---

## 🤝 Contributing

Contributions are welcome and encouraged.

Steps to contribute:

1. Fork the repository  
2. Create a new branch  
3. Make your changes  
4. Submit a pull request  

You can contribute by improving features, fixing bugs, enhancing UI, or optimizing performance.

---

## 📜 License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

---

## ⭐ Support

If you find this project useful, consider giving it a star on GitHub.

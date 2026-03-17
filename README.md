<!DOCTYPE html>
<html lang="en">
<body>

 # Intelligent Agent Based Job Search System

<p>
A Django-based web application that intelligently matches job seekers with relevant job opportunities by analyzing uploaded resumes using Natural Language Processing (NLP) and fuzzy skill matching.
</p>

<hr>

<h2>📌 Features</h2>
<ul>
  <li><b>Resume Upload & Parsing</b> – Upload a PDF resume and automatically extract text using <code>pypdf</code></li>
  <li><b>NLP-Based Skill Extraction</b> – Uses <code>spaCy</code> with a curated skills dataset to identify relevant skills</li>
  <li><b>Fuzzy Skill Matching</b> – Matches extracted skills with job descriptions using <code>rapidfuzz</code></li>
  <li><b>Smart Job Recommendations</b> – Ranks jobs based on skill match percentage</li>
  <li><b>Paginated Job Listings</b> – Browse jobs efficiently with pagination</li>
  <li><b>Excel-Based Data Source</b> – Job listings loaded using <code>pandas</code></li>
  <li><b>User Authentication</b> – Register and login functionality</li>
  <li><b>Django Admin Panel</b> – Manage jobs, resumes, and portals</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>
<table border="1" cellpadding="8">
<tr><th>Layer</th><th>Technology</th></tr>
<tr><td>Backend Framework</td><td>Django</td></tr>
<tr><td>NLP</td><td>spaCy (en_core_web_sm)</td></tr>
<tr><td>Fuzzy Matching</td><td>RapidFuzz</td></tr>
<tr><td>PDF Parsing</td><td>pypdf</td></tr>
<tr><td>Data Processing</td><td>pandas, openpyxl</td></tr>
<tr><td>Database</td><td>SQLite3</td></tr>
<tr><td>Language</td><td>Python 3.10+</td></tr>
</table>

<hr>

<h2>📁 Project Structure</h2>
<pre>
job_search_system/
├── job_search/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── data/
│   │   └── job_data.xlsx
│   ├── templates/
│   │   ├── job_search/
│   │   └── registration/
│   └── migrations/
├── job_search_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
├── scripts/
│   ├── skills_db.json
│   └── excel_sheet_update_standalone.py
├── manage.py
└── db.sqlite3
</pre>

<hr>

<h2>🚀 Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.10+</li>
  <li>pip</li>
</ul>

<h3>Installation</h3>

<ol>
  <li><b>Clone the repository</b></li>
</ol>
<pre>
git clone https://github.com/your-username/job_search_system.git
cd job_search_system
</pre>

<ol start="2">
  <li><b>Create virtual environment</b></li>
</ol>
<pre>
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate
</pre>

<ol start="3">
  <li><b>Install dependencies</b></li>
</ol>
<pre>
pip install django spacy rapidfuzz pypdf pandas openpyxl
</pre>

<ol start="4">
  <li><b>Download spaCy model</b></li>
</ol>
<pre>
python -m spacy download en_core_web_sm
</pre>

<ol start="5">
  <li><b>Apply migrations</b></li>
</ol>
<pre>
python manage.py migrate
</pre>

<ol start="6">
  <li><b>Run the server</b></li>
</ol>
<pre>
python manage.py runserver
</pre>

<ol start="7">
  <li><b>Open in browser</b></li>
</ol>
<pre>
http://127.0.0.1:8000/
</pre>

<hr>

<h2>⚙️ How It Works</h2>
<ol>
  <li>User uploads a PDF resume</li>
  <li>Text is extracted using pypdf</li>
  <li>spaCy processes the text</li>
  <li>Skills are matched using fuzzy matching</li>
  <li>Job descriptions are compared with extracted skills</li>
  <li>Jobs are ranked based on match percentage</li>
  <li>Results are displayed to the user</li>
</ol>

<hr>

<h2>📊 Data Source</h2>

<p>Job data is stored in:</p>
<pre>job_search/data/job_data.xlsx</pre>

<table border="1" cellpadding="8">
<tr><th>Column</th><th>Description</th></tr>
<tr><td>Job Role</td><td>Title of the job</td></tr>
<tr><td>Company Name</td><td>Hiring company</td></tr>
<tr><td>Job Description</td><td>Full description</td></tr>
<tr><td>Job URL</td><td>Link to job details</td></tr>
<tr><td>Apply URL</td><td>Application link</td></tr>
</table>

<hr>

<h2>🗄️ Database Models</h2>
<ul>
  <li><b>Job</b> – Stores job details and descriptions</li>
  <li><b>Resume</b> – Stores uploaded resumes and extracted skills</li>
  <li><b>CareerPortal</b> – Stores company portal information</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>

<p>All developers are welcome to contribute to this project.</p>

<ol>
  <li>Fork the repository</li>
  <li>Create a new branch</li>
  <li>Make your changes</li>
  <li>Submit a pull request</li>
</ol>

<p>You can contribute by improving features, optimizing performance, enhancing UI/UX, or adding new ideas.</p>


<h2>⭐ Support</h2>

<p>If you find this project useful, consider giving it a ⭐ on GitHub!</p>

</body>
</html>

import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# List of job URLs
job_urls = []
job_data = []  # Define the job_data list here

base_url = []
# Step 1: Scrape the job listing page to get individual job links
for page_num in range(1, 6):  # For pages 1 to 5
    url = f"{base_url}?page={page_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all job links (adjust selector to match the site's structure)
    job_anchors = soup.find_all('a', class_='job-apply')  # Update class if needed
    for link in job_anchors:
        job_urls.append(link.get('href'))

    base_url = []
    job_urls = [urljoin(base_url, link) for link in job_urls]
print("urls", job_urls)


for job_url in job_urls:
    job_response = requests.get(job_url)
    job_soup = BeautifulSoup(job_response.content, 'html.parser')

    # Extract job description
    job_description_div = job_soup.find('div', class_='jd-content')
    if job_description_div:
        job_description = job_description_div.text.strip()
    else:
        job_description = "Job description not found."
    
    # Extract the job title
    job_title = job_soup.find('p', class_='position').text.strip()

    job_title = job_soup.find('p', class_='position').text.strip()
    # Extract the company name
    company_name = job_soup.find('p', class_='company-name').text.strip()
    apply_now_div = job_soup.find_all('div', class_='apply-main')
    if apply_now_div:
        apply_now_url = apply_now_div[2].find('a')['href']
        apply_now_url = urljoin(job_url, apply_now_url)  # Make it an absolute URL
    else:
        apply_now_url = "Apply URL not found."
    

    # Print extracted information
    # print(job_title, company_name, job_description)
    
    # Append the data to job_data list
    if job_title and company_name and job_description:
        job_data.append({
            'Job Role': job_title,
            'Company Name': company_name,
            'Job Description': job_description,
            'Job URL' : job_url,
            'Apply URL' : apply_now_url
        })

# Step 3: Save the data to an Excel file
df = pd.DataFrame(job_data)
df.to_excel(r'job_search\\data\\job_data.xlsx', index=False)

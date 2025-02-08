from django import forms
from .models import Resume
import openpyxl

# ModelForm for the Resume upload
class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['user_name', 'uploaded_file']

    # Optional: Custom validation or fields for extracted skills
    # You can add other methods if you want to validate or clean the data
    def clean_uploaded_file(self):
        file = self.cleaned_data.get('uploaded_file')
        # Here you can add custom validation if you want (e.g., file type checks)
        return file
class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()

    # Optional: You can add validation to check if the uploaded file is indeed an Excel file
    def clean_excel_file(self):
        file = self.cleaned_data.get('excel_file')
        # You could add a check here for the file type if needed
        return file
# forms.py
from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'experiece' ,'description', 'required_skills']

    def clean_required_skills(self):
        skills = self.cleaned_data['required_skills']
        # Add custom validation logic if needed
        return skills


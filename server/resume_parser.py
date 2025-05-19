import re
import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-\(\)]{7,}\d', text)
    return match.group(0) if match else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text):
    # Very basic keyword matching, can be improved
    skills_keywords = ['python', 'java', 'sql', 'javascript', 'html', 'css', 'flask', 'django', 'react', 'node']
    found_skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    return found_skills

def parse_resume(file_path):
    from pdfminer.high_level import extract_text
    text = extract_text(file_path)
    print("\n\n=========== Extracted Text ===========")
    print(text)
    print("======================================\n\n")
    return {
        "Name": None,
        "Email": None,
        "Phone": None,
        "Skills": []
    }


import re
import PyPDF2

def parse_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        page_obj = pdf_reader.getPage(0)
        resume_text = page_obj.extractText()
        return parse_resume(resume_text)

def parse_resume(resume_text):
    # Extract name
    name_regex = re.compile(r"^Name:\s+(.+)$", re.MULTILINE)
    match = name_regex.search(resume_text)
    if match:
        name = match.group(1)
    else:
        name = None

    # Extract email
    email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    email = email_regex.search(resume_text)
    if email:
        email = email.group(0)
    else:
        email = None

    # Extract phone number
    phone_regex = re.compile(r"((?:\d{3}-)|(?:\d{3}\s))?\d{3}-\d{4}")
    phone = phone_regex.search(resume_text)
    if phone:
        phone = phone.group(0)
    else:
        phone = None

    # Extract skills
    skills_regex = re.compile(r"Skills:\s+(.+)$", re.MULTILINE)
    match = skills_regex.search(resume_text)
    if match:
        skills = match.group(1).split(",")
    else:
        skills = []

    # Extract experience
    experience_regex = re.compile(r"Experience:\s+(.+)$", re.MULTILINE)
    match = experience_regex.search(resume_text)
    if match:
        experience = match.group(1)
    else:
        experience = None

    # Extract education
    education_regex = re.compile(r"Education:\s+(.+)$", re.MULTILINE)
    match = education_regex.search(resume_text)
    if match:
        education = match.group(1)
    else:
        education = None

    # Return extracted information
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "experience": experience,
        "education": education
    }

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    extracted_info = parse_pdf(pdf_path)
    print(extracted_info)
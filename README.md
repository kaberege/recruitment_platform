
## Recruitment Platform API

A robust recruitment/job portal backend built with Django and Django REST Framework (DRF). This platform allows job seekers and recruiters to interact — from creating profiles and posting jobs to applying and managing applications. The project features role-based authentication using JWT, and is ready for frontend extensions with React or mobile applications. Deployment is handled via PythonAnywhere.

🚀 Features
🔐 Authentication & User Management
JWT-based authentication (Login, Logout, Register)

Email verification and secure password reset

Role-based user accounts: Job Seeker, Recruiter, and Admin

Optional social login (Google, LinkedIn)

👤 User Profiles
Job Seekers: Name, bio, education, experience, resume upload

Recruiters: Company info, logo, website

💼 Job Management (Recruiters)
Create, edit, and delete job listings

Fields: title, description, requirements, location, type, salary, deadline

View applicants and their statuses

🔍 Job Browsing & Applications (Job Seekers)
Search and filter jobs by location, type, salary, keywords

Apply to jobs with resume and cover letter

Track application status

📬 Notifications & Messaging
Email notifications on key events (application submitted, status change)

📊 Dashboards
Job Seekers: Profile completion, application history

Recruiters: Job posts overview, applicant list, resume access

🛠️ Admin Panel
Full user, job, and application management

View analytics and moderate content

🧱 Tech Stack
Layer	Tools Used
Backend	Django, Django REST Framework
Auth	JWT (djangorestframework-simplejwt)
Database	SQLite (dev) / PostgreSQL (prod)
Testing	Postman
Deployment	PythonAnywhere
Versioning	Git, GitHub

🔗 Data Relationships
User → OneToOne → JobSeekerProfile or RecruiterProfile

RecruiterProfile → OneToMany → Job

Job → ManyToMany (via Application) → JobSeekerProfile

📦 Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/yourusername/recruitment-platform.git
cd recruitment-platform

# Create virtual environment & activate
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
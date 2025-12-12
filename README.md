# **Recruitment Platform API**

A scalable and secure recruitment/job portal backend built using **Django** and **Django REST Framework (DRF)**.
The platform enables seamless interaction between **Job Seekers** and **Recruiters**, supporting user authentication, profile management, job posting, applications, and more.
It uses **JWT authentication**, follows modular app structure, and is ready for integration with **React**, **Next.js**, or mobile clients.

---

## **Core Features**

### **Authentication & Authorization**

- Custom user model using email as the login field
- User roles:

  - **Job Seeker**
  - **Recruiter**
  - **Admin (superuser)**

- JWT authentication (`djangorestframework-simplejwt`)
- Token blacklisting for secure logout
- Password hashing and validation using Django standards

---

### **User Profiles**

Separate profile models for different roles:

#### **Job Seeker Profile**

- Personal info
- Bio, education, experience
- Resume upload
- Associated job applications

#### **Recruiter Profile**

- Company information
- Company logo and website
- Manages posted jobs

---

### **Job Management (Recruiters)**

Recruiters can:

- Create, update, and delete job posts
- Include fields such as:

  - Title, description, requirements
  - Location, job type, salary range
  - Application deadline

- View applications submitted to each job

---

### **Job Browsing & Applications (Job Seekers)**

Job seekers can:

- Browse and filter job listings
- Submit applications with resume & optional cover letter
- Track application statuses:

  - `submitted`
  - `under_review`
  - `shortlisted`
  - `rejected`
  - `accepted`

Duplicate applications are automatically prevented.

---

### **Admin Panel**

Django Admin allows:

- Full management of users, profiles, jobs, and applications
- Moderation and basic analytics

---

## 🧱 **Tech Stack**

| Layer               | Technologies                                                |
| ------------------- | ----------------------------------------------------------- |
| **Backend**         | Django, Django REST Framework                               |
| **Authentication**  | JWT (SimpleJWT)                                             |
| **Database**        | SQLite (dev), PostgreSQL/MySQL (recommended for production) |
| **Documentation**   | drf-yasg (Swagger UI, ReDoc)                                |
| **CORS**            | django-cors-headers                                         |
| **Deployment**      | PythonAnywhere                                              |
| **Version Control** | Git + GitHub                                                |

---

## **Data Model Overview**

```
User (Custom)
   |
   ├── OneToOne → JobSeekerProfile
   |
   └── OneToOne → RecruiterProfile

RecruiterProfile
   |
   └── OneToMany → Job

Job
   |
   └── OneToMany → JobSeekerApplication

JobSeekerProfile
   |
   └── OneToMany → JobSeekerApplication
```

---

## **Project Structure**

```
recruitment_platform/
│
├── users/             # Custom user model, auth, managers
├── profiles/          # JobSeeker and Recruiter profiles
├── applications/      # Job applications
├── templates/         # Swagger templates (if any)
├── mystaticfiles/     # Static assets for development
├── productionfiles/   # Static assets for production (Whitenoise)
│
├── manage.py
└── requirements.txt
```

---

## **Environment & Configuration**

Key technologies configured in `settings.py`:

### **Authentication**

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

### **JWT**

```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}
```

### **CORS**

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
    "https://mohamdah-aa-frontend.netlify.app",
]
```

---

## **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/kaberege/recruitment_platform.git
cd recruitment_platform
```

### **2. Create and Activate a Virtual Environment**

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**

```bash
python manage.py migrate
```

### **5. Run Development Server**

```bash
python manage.py runserver
```

---

## **API Documentation (Swagger & ReDoc)**

After running the server, visit:

- Swagger UI → `/swagger/`
- ReDoc → `/redoc/`

Powered by **drf-yasg**.

---

## **Testing**

You may test all endpoints using:

- Postman
- Swagger UI
- Thunder Client (VS Code)

---

## **Deployment**

Configured for **PythonAnywhere** using:

- Whitenoise for static files
- Production-optimized settings

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Creates users and superusers
class MyUserManager(BaseUserManager):
    def create_user(self, email, role, password=None, **other_fields):
        if not email:
            raise ValueError("Users must have an email address!")
        if not password:
            raise ValueError("Password is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, role, password=None, **other_fields):
        user = self.create_user(email, role, password=password, **other_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

# Defines custom user
class MyUser(AbstractUser):
    ROLE_CHOICES = [
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter')
    ]

    username = models.CharField(unique=False, max_length=255)
    email = models.EmailField(unique=True, blank=False, null=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"  # Replace username field with email field
    REQUIRED_FIELDS = ['role']  # Add role field to the riquired fields
    objects = MyUserManager()

    def __str__(self):
        return f'{self.email}: A {self.role}'

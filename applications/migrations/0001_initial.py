# Generated by Django 5.2.1 on 2025-05-22 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('internship', 'Internship')], max_length=50)),
                ('salary_range', models.CharField(blank=True, max_length=100)),
                ('deadline', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='profiles.recruiterprofile')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeekerApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='applications/resumes/')),
                ('cover_letter', models.FileField(blank=True, null=True, upload_to='applications/letters/')),
                ('status', models.CharField(choices=[('submitted', 'Submitted'), ('under_review', 'Under Review'), ('shortlisted', 'Shortlisted'), ('rejected', 'Rejected'), ('accepted', 'Accepted')], default='submitted', max_length=20)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='profiles.jobseekerprofile')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='applications.job')),
            ],
            options={
                'unique_together': {('job', 'applicant')},
            },
        ),
    ]

from django.contrib import admin
from .models import Job, JobSeekerApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'recruiter', 'location', 'job_type', 'salary_range', 'deadline', 'created_at')
    list_filter = ('job_type', 'location', 'deadline', 'created_at')
    search_fields = ('title', 'recruiter__user__username', 'location', 'description', 'requirements')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(JobSeekerApplication)
class JobSeekerApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('job__title', 'applicant__user__username', 'applicant__user__email')
    readonly_fields = ('applied_at',)

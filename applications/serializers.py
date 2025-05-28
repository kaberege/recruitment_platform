from datetime import date
from rest_framework import serializers
from .models import JobSeekerApplication, Job
import os

class JobSerializer(serializers.ModelSerializer):
    recruiter = serializers.ForeignKeyRelatedFieald(read_only=True)
    salary_range = serializers.CharField(required=False)
    deadline = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S', read_only=True)

    class Meta:
        model = Job
        fields = '__all__'

    def validate_deadline(self, value):
        if value < date.today():
            raise serializers.ValidationError("Deadline cannot be in the past.")
        return value

class JobSeekerApplicationSerializer(serializers.ModelSerializer):
    job = serializers.ForeignKey(queryset=Job.objects.all())
    applicant = serializers.ForeignKeyRelatedFieald(read_only=True)
    cover_letter = serializers.FileField(required=False)
    applied_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S')

    class Meta:
        model = JobSeekerApplication
        fields = '__all__'

    read_only_fields = ['status', 'applied_at']

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    def validate_file_extension(self, file):
        valid_extensions = ['.pdf', '.docx']
        ext = os.path.splitext(file.name)[1].lower()
        if ext not in valid_extensions:
            raise serializers.ValidationError("Only PDF and DOCX files are allowed.")
        if file.size > MAX_FILE_SIZE:
            raise serializers.ValidationError("File size should not exceed 5MB.")
        return file

    def validate_resume(self, value):
        return self.validate_file_extension(value)

    def validate_cover_letter(self, value):
        if value:
            return self.validate_file_extension(value)
        return value
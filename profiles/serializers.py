from rest_framework import serializers
from .models import JobSeekerProfile, RecruiterProfile
from django.contrib.auth import get_user_model

User = get_user_model()  # Custom user

# Serializer class for Job seeker
class JobSeekerProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    picture = serializers.ImageField(required=False, allow_null=True)
    website = serializers.URLField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S', read_only=True)

    class Meta:
        model = JobSeekerProfile
        fields = "__all__"

# Serializer class for Recruiter
class RecruiterProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    company_website = serializers.URLField(required=False, allow_null=True)
    company_logo = serializers.ImageField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S', read_only=True)

    class Meta:
        model = RecruiterProfile
        fields = "__all__"
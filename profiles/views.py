from django.shortcuts import render, get_object_or_404
from rest_framework import status,viewsets
from .serializers import JobSeekerProfileSerializer, RecruiterProfileSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsRecruiter, IsStaff
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from .models import JobSeekerProfile, RecruiterProfile

# Job seeker view
class JobSeekerProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = JobSeekerProfileSerializer
    queryset = JobSeekerProfile.objects.all()

    def get_queryset(self):
        job_seeker = self.request.user
        user = JobSeekerProfile.objects.filter(user=job_seeker)
        return user

    def perform_create(self, serializer):
        user = self.request.user
        # Check if the user has already a profile
        if JobSeekerProfile.objects.filter(user=user).exists():
            raise PermissionDenied("You already have a profile. You cannot create multiple profiles.")

        serializer.save(user=user)

    def perform_update(self, serializer):
        # Checking if the user is the owner of the custom profile before updating
        if self.get_object().user != self.request.user:
            raise PermissionDenied("You can only update your own profile.")

        serializer.save()
        
    def perform_destroy(self, instance):
        # Checking if the user is the owner of the custom profile before deleting
        if instance.user != self.request.user:
            raise PermissionDenied("You can only delete your own profile")

        instance.delete()

# Recruiter view
class RecruiterProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsRecruiter | IsStaff]
    serializer_class = RecruiterProfileSerializer
    queryset = RecruiterProfile.objects.all()

    def get_queryset(self):
        recruiter = self.request.user
        user = RecruiterProfile.objects.filter(user=recruiter)
        return user

    def perform_create(self, serializer):
        user = self.request.user
        # Check if the user has already a profile
        if RecruiterProfile.objects.filter(user=user).exists():
            raise PermissionDenied("You already have a profile. You cannot create multiple profiles.")

        serializer.save(user=user)
from rest_framework import status,viewsets
from .serializers import JobSeekerApplicationSerializer, JobSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from .models import JobSeekerApplication, Job

# Job view
class JobViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class =  JobSerializer
    queryset = Job.objects.all()

    def perform_create(self, serializer):
        recruiter = self.request.user["role"]
        serializer.save(recruiter=recruiter)

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


""" from rest_framework import viewsets, permissions
from .models import Job, JobSeekerApplication
from .serializers import JobSerializer, JobSeekerApplicationSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        recruiter_profile = self.request.user.recruiter_profile
        serializer.save(recruiter=recruiter_profile)


class JobSeekerApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobSeekerApplication.objects.all()
    serializer_class = JobSeekerApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        job_seeker_profile = self.request.user.job_seeker_profile
        serializer.save(applicant=job_seeker_profile)
 """
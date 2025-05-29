from rest_framework import status, viewsets
from .serializers import JobSeekerApplicationSerializer, JobSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from .models import JobSeekerApplication, Job
from .permissions import IsJobPoster, IsJobApplicant

# Job view
class JobViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsJobPoster]
    serializer_class =  JobSerializer
    queryset = Job.objects.all()

    def perform_create(self, serializer):
        try:
            recruiter_profile = self.request.user.recruiter_profile
            serializer.save(recruiter=recruiter_profile)
        except Exception as error:
            raise PermissionDenied(f'{error} You have to create recruiter profile.')

# Job seeker application view
class JobSeekerApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsJobApplicant]
    serializer_class = JobSeekerApplicationSerializer
    queryset = JobSeekerApplication.objects.all()

    def get_queryset(self):
        try:
            job_seeker_profile = self.request.user.job_seeker_profile
            applicant = JobSeekerApplication.objects.filter(applicant=job_seeker_profile)
            return applicant
        except Exception as error:
            raise PermissionDenied(f'{error} You have to create a job seeker profile.')

    def perform_create(self, serializer):
        try:
            job_seeker_profile = self.request.user.job_seeker_profile
            serializer.save(applicant=job_seeker_profile)
        except Exception as error:
            raise PermissionDenied(f'{error} You have to create a job seeker profile.')

from django.urls import path, include
from rest_framework import routers
from .views import JobSeekerProfileViewSet, RecruiterProfileViewSet

# Initialize a DefaultRouter, which will automatically generate URL patterns for viewsets
router = routers.DefaultRouter()

""" Register the JobSeekerProfileViewSet with the router, 
this will create the appropriate URLs for JobSeekerProfile CRUD operations """
router.register(r'seeker', JobSeekerProfileViewSet, basename="seeker-profile")

""" Register the RecruiterProfileViewSet with the router, 
this will create the appropriate URLs for RecruiterProfile CRUD operations """
router.register(r'recruiter', RecruiterProfileViewSet, basename="recruiter-profile")

urlpatterns = [
    path("job/", include(router.urls)),  
]
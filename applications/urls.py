from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, JobSeekerApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename="posted-jobs")
router.register(r'applications', JobSeekerApplicationViewSet, basename="applicant-details")

urlpatterns = [
    path("", include(router.urls)),   
]

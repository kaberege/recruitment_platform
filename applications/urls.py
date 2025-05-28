from django.urls import path

urlpatterns = [
    
]
""" 
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, JobSeekerApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'applications', JobSeekerApplicationViewSet)

urlpatterns = router.urls
 """
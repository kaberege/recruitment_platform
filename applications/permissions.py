from rest_framework.permissions import BasePermission

# Allows job modification to the recruiter.
class IsJobPoster(BasePermission):
    message = "Permission denied because you did not create this job." # Custom error message

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if obj.recruiter == self.request.user.recruiter_profile:
            return True
        return False

# Allows access only to job seekers.
class IsJobApplicant(BasePermission):
    message = "Permission denied because you did not apply to this job." # Custom error message

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if obj.applicant == self.request.user.job_seeker_profile:
            return True
        return False
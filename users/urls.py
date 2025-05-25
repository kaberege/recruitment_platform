from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterUserView, LoginUserView, UpdateUserView, DeleteUserView, LogoutUserView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("update/", UpdateUserView.as_view(), name="update"),
    path("delete/", DeleteUserView.as_view(), name="delete"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
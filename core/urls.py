from django.urls import path
from core.views import anonymous_auth, join_channel

urlpatterns = [
    path("auth/", anonymous_auth),
    path("join/", join_channel),
]
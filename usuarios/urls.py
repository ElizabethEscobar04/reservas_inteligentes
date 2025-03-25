from django.urls import path
from .views import RegistroUsuarioView

urlpatterns = [
    path('register/', RegistroUsuarioView.as_view(), name='register'),
]
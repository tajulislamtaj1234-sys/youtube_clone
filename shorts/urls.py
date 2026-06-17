from django.urls import path
from .views import ShortsView

urlpatterns = [
    path('', ShortsView.as_view(), name='shorts'),
]
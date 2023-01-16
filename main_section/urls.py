from django.urls import path
from main_section.views import ContactView


urlpatterns = [
    path('', ContactView.as_view(), name='main-home'),
]
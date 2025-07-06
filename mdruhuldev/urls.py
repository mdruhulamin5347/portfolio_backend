from django.urls import path
from .views import *
urlpatterns = [
    path('home/', HomeSectionView.as_view(), name='home-section'),
    path('about/', AboutSectionView.as_view(), name='about-section'),
    path('experience/', WorkExperienceView.as_view(), name='work-experience'),
    path('education/', EducationSectionView.as_view(), name='education-section'),
    path('certification/', CertificationSectionView.as_view(), name='certification-section'),
    path('skills/', SkillSectionView.as_view(), name='skill-section'),
    path('services/', ServiceSectionView.as_view(), name='service-section'),
    path('projects/', ProjectSectionView.as_view(), name='project-section'),
    path('location/', LocationSectionView.as_view(), name='location-section'),
    path('messages/', ContactMessageView.as_view(), name='contact-messages'),
]
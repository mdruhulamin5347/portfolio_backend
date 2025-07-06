from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.core.mail import send_mail
from .models import *
from .serializers import *


class HomeSectionView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = HomeSection.objects.first()
        serializer = HomeSectionSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)


class AboutSectionView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = AboutSection.objects.first()
        serializer = AboutSectionSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)


class WorkExperienceView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = WorkExperience.objects.all()
        serializer = WorkExperienceSerializer(data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class EducationSectionView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = EducationSection.objects.all()
        serializer = EducationSectionSerializer(data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class CertificationSectionView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = CertificationSection.objects.all()
        serializer = CertificationSectionSerializer(data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class SkillSectionView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = SkillSection.objects.all()
        serializer = SkillSectionSerializer(data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class ServiceSectionView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = ServiceSection.objects.all()
        serializer = ServiceSectionSerializer(data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class ProjectSectionView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = ProjectSection.objects.all()
        serializer = ProjectSectionSerializer(data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class LocationSectionView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = LocationSection.objects.first()
        serializer = LocationSectionSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)



class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Send Email
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']

            send_mail(
                subject=f"New message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email='no-reply@mdruhuldev.com',
                recipient_list=['myprojects.helpservice@gmail.com'],
                fail_silently=False,
            )

            return Response({"message": "Message sent successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

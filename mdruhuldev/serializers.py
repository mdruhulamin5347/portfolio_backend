from rest_framework import serializers
from .models import *

class HomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSection
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class WorkExperienceSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = WorkExperience
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class EducationSectionSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = EducationSection
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class CertificationSectionSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = CertificationSection
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class SkillSectionSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = SkillSection
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class ServiceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSection
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class ProjectSectionSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = ProjectSection
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class LocationSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationSection
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        # fields = '__all__'
        exclude = ['id','status','created_at','updated_at']
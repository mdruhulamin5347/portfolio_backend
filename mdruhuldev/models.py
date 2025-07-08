from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class HomeSection(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    github_link = models.URLField(max_length=500, null=True, blank=True)
    linkedin_link = models.URLField(max_length=500, null=True, blank=True)
    resume_download = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"name: {self.name} - title: {self.title}"



class AboutSection(BaseModel):
    title = models.CharField(max_length=250, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='about/', default='default.jpg')

    def __str__(self):
        return self.title or "About Section"




class Technology(BaseModel):
    section = models.CharField(max_length=150,null=True,blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name




class WorkExperience(BaseModel):
    company = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100, null=True, blank=True)  # or "Present"
    responsibilities = models.TextField()
    technologies = models.ManyToManyField(Technology, blank=True, related_name='work_technologies')

    def __str__(self):
        return f"{self.position} at {self.company}"




class EducationSection(BaseModel):
    degree = models.CharField(max_length=250, null=True, blank=True)
    duration = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    course_name = models.CharField(max_length=500, null=True, blank=True)
    institute = models.CharField(max_length=500, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True, related_name='education_technologies')




class CertificationSection(BaseModel):
    degree = models.CharField(max_length=250, null=True, blank=True)
    duration = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    course_name = models.CharField(max_length=500, null=True, blank=True)
    institute = models.CharField(max_length=500, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True, related_name='certification_technologies')




class SkillSection(BaseModel):
    title = models.CharField(max_length=150, null=True, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True, related_name='skill_technologies')
    icon = models.CharField(max_length=100, null=True, blank=True)  
    def __str__(self):
        return self.title



class ServiceSection(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    step_1 = models.CharField(max_length=250,null=True,blank=True)
    step_2 = models.CharField(max_length=250,null=True,blank=True)
    step_3 = models.CharField(max_length=250,null=True,blank=True)
    step_4 = models.CharField(max_length=250,null=True,blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)  

    def __str__(self):
        return self.title




class ProjectSection(BaseModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, blank=True, related_name='project_technologies')
    github_link = models.URLField(max_length=500, null=True, blank=True)
    live_demo_link = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)

    def __str__(self):
        return self.title



class LocationSection(BaseModel):
    email = models.EmailField(null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f"{self.email} - {self.location}"




class ContactMessage(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"
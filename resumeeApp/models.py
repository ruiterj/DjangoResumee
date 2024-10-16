from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    personal_summary = models.TextField(blank=True, null=True)  # New field
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # New field
    skills = models.TextField()
    work_experiences = models.TextField()
    educations = models.TextField()
    selected_template = models.CharField(max_length=10)
    selected_color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

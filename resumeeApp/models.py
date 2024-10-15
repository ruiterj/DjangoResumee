from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    skills = models.TextField()
    work_experiences = models.TextField()
    educations = models.TextField()
    selected_template = models.CharField(max_length=10)
    selected_color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

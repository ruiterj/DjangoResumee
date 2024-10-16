# Generated by Django 5.1.1 on 2024-10-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeeApp', '0002_alter_resume_selected_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='personal_summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]

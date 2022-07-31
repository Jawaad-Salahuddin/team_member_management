from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=25)
    role = models.CharField(max_length=10, choices=[('regular','Regular - Can\'t delete members'),('admin','Admin - Can delete members')])

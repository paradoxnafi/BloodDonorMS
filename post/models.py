from django.db import models

BLOOD_GROUPS = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class Post(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    blood_group = models.CharField(max_length=8, choices=BLOOD_GROUPS, default='O+')


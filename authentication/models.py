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

class Register(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=250, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nid = models.CharField(max_length=13, null=True, blank=True)
    blood_group = models.CharField(max_length=8, choices=BLOOD_GROUPS, default='O+', null=True, blank=True)
    
    def __str__(self):
        return self.username

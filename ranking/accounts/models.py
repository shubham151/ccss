from django.db import models
from  django.contrib.auth.models import User
from django.db.models.signals import post_save


class Questions(models.Model):
    question = models.CharField(max_length=200)
    lang_choice= (
        ('C', 'C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('PHP', 'PHP'),
        ('JAVA', 'JAVA'),
        ('PYTHON', 'PYTHON'),
    )
    language = models.CharField(max_length=50, choices=lang_choice, default='C')


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.IntegerField()
    qualification = models.CharField(max_length=50)
    age=models.IntegerField()
    experience = models.CharField(max_length=50)




# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile =


# post_save.connect(create_profile, sender=User)
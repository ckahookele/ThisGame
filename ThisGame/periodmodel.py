from django.db import models

class Fact(models.Model):
    block = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    teacher = models.ForeignKey('Teacher.name')
    classes = models.ForeignKey('Class.name')
    subject = models.ForeignKey('Subject.name')
    

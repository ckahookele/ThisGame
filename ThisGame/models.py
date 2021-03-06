from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)

class Class(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

class Subject(models.Model):
    name = models.CharField(max_length=255)

class Period(models.Model):
    block = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    teacher = models.ForeignKey('ThisGame.Teacher')
    claz = models.ForeignKey('ThisGame.Class')
    subject = models.ForeignKey('ThisGame.Subject')
    

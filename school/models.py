from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    birth = models.DateField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('M', 'Medium'),
        ('A', 'Advanced')
    )
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    
    level = models.CharField(
        max_length=1, 
        choices=LEVEL, 
        blank=False, 
        null=False, 
        default='B'
        )


    def __str__(self):
        return self.description
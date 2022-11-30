from django.db import models

from django.contrib.auth.models import User


def user_directory_path(instance, filename): 
    name = filename.split(".")
    
    name = instance.firstname + instance.lastname
    filename = name + ".JPG"
    return 'Faculty_Images/{}'.format(filename)

class Faculty(models.Model):

    user = models.OneToOneField(User, null = True, blank = True, on_delete= models.CASCADE)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to=user_directory_path ,null=True, blank=True)

    def __str__(self):
        return str(self.firstname + " " + self.lastname)


def student_directory_path(instance, filename): 
    #name = filename.split(".")
    
    name = instance.registration_id 
    
    filename = name + ".jpg" 
    return 'Student_Images/{}/{}'.format(instance.branch,filename)

class Student(models.Model):

    BRANCH = (
        ('CSE','CSE'),
        ('IT','IT'),
        ('ECE','ECE'),
        ('CHEM','CHEM'),
        ('MECH','MECH'),
        ('EEE','EEE'),
    )
   
   
    

    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    registration_id = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=100, null=True, choices=BRANCH)
  
    profile_pic = models.ImageField(upload_to=student_directory_path ,null=True, blank=True)


    def __str__(self):
        return str(self.registration_id)

class Attendence(models.Model):
    
    Faculty_Name = models.CharField(max_length=200, null=True, blank=True)
    Student_ID = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add = True, null = True)
    time = models.TimeField(auto_now_add=True, null = True)
    branch = models.CharField(max_length=200, null = True)
   
    period = models.CharField(max_length=200, null = True)
    status = models.CharField(max_length=200, null = True, default='Absent')

    def __str__(self):
        return str(self.Student_ID + "_" + str(self.date)+ "_" + str(self.period))
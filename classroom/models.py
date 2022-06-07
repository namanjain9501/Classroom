from pickle import TRUE
from django.contrib.auth.models import AbstractUser
from django.db import models

class Standard(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('username',)

#     def _str_(self):
#         return self.username

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    standard = models.ForeignKey(Standard,null=TRUE, on_delete=models.SET_NULL)


# class Task(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
    
# class Answer(models.Model):
#     student_name = models.ForeignKey(User, on_delete=models.CASCADE, default=User.id)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)(max_length=50)
#     Answer = models.TextField()
    
class Assignment(models.Model):
    name = models.CharField(max_length=1000, default='')
    description = models.TextField(max_length=1000, default='')
    post_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Submission(models.Model):  
    submission = models.TextField()
    time_submitted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.user)





class Students(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1, primary_key=True)
    standard = models.ForeignKey(Standard,null=TRUE, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.user)

from asyncio import Task
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms
from django.forms import ModelForm

# class TeacherTaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ('name','description')

class SubmissionForm(forms.ModelForm):
    submission = forms.CharField(
        widget= forms.Textarea(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Write your details here... ",
                "rows":"7"

            }
        )
    )
    class Meta:
        model = Submission
        fields = ['submission']




class AssignmentForm(forms.ModelForm):

    name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter Name of Your Task"

            }
        )
    )



    deadline = forms.DateTimeField(
        widget= forms.DateTimeInput(
            attrs={
                "class": "form-control", 
                "type": "datetime-local",
           
            }
        )
    )

    standard = forms.ModelChoiceField(queryset=Standard.objects.all(), 
    widget= forms.Select(
            attrs={
                "class": "form-control", 
            }
        )

    )

    description = forms.CharField(
        widget= forms.Textarea(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Describe Your Task Here... ",
                "rows":"4"

            }
        )
    )

  

    class Meta:
        model = Assignment
        fields = ['standard','name','description', 'deadline']


class loginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input",
                "type": "text",
                "placeholder": "Enter firstname"

            }
        )
    )

    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input",
                "type": "text",
                "placeholder": "Enter Lastname"
            }
        )
    )
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter Username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Enter Email-id"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Enter Password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Re-enter Password"
    }))
    

    

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')


class StudentRegistration(UserCreationForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input",
                "type": "text",
                "placeholder": "Enter firstname"

            }
        )
    )

    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input",
                "type": "text",
                "placeholder": "Enter Lastname"
            }
        )
    )
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter Username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Enter Email-id"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Enter Password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Re-enter Password"
    }))


    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2','standard')

class StudentClassUpdate(forms.ModelForm):


    class Meta:
        model = Students
        fields = ['standard']

class UpdateStudentForm(forms.ModelForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input",
                "type": "text",
                "placeholder": "Enter firstname"

            }
        )
    )

    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input",
                "type": "text",
                "placeholder": "Enter Lastname"
            }
        )
    )

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Enter Email-id"
    }))

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email','standard')


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input",
                "type": "text",
                "placeholder": "Enter firstname"

            }
        )
    )

    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input",
                "type": "text",
                "placeholder": "Enter Lastname"
            }
        )
    )

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Enter Email-id"
    }))

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email')


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ("username","email")

# class CustomUserChangeForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ("username","email")





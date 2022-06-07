from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
import datetime

# Create your views here.

def home(request):
    return render(request, 'home.html')           
 

# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             if user.is_student:
#                 student_form = StudentRegistration()
#                 return render(request,'class.html',{'student_form':student_form, 'user':user})

#             messages.success(request, ("User Registered"))
#             return redirect('login')
            
#         else:
#             messages.success(request, ("Form is invalid!"))
#             return redirect('register')
#     else: 
#         form = SignUpForm()        
#         return render(request,'register.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.save()
            messages.success(request, ("Admin Registered Successfully"))
            return redirect('login')
            
        else:
            messages.success(request, ("Form is invalid!"))
            return redirect('register')
    else: 
        form = SignUpForm()        
        return render(request,'register.html',{'form':form})




def add_teacher(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_teacher = True
            user.save()
            messages.success(request, ("Teacher Registered Successfully"))
            return redirect('teacher-list')
            
        else:
            messages.success(request, ("Form is invalid!"))
            return redirect('teacher-list')
    else: 
        form = SignUpForm()        
        return render(request,'add_teacher.html',{'form':form})





def add_student(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            messages.success(request, ("Student Added Successfully"))
            return redirect('student-list')
            
        else:
            messages.success(request, ("Form is invalid!"))
            return redirect('add_student')
    else: 
        form = StudentRegistration()        
        return render(request,'add_student.html',{'form':form})


def login_view(request):
    form = loginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = authenticate(username=User.objects.get(email=username), password=password)
            except:
                user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, ("Invalid Credentials!"))
                return redirect('login')
        else:
            messages.success(request, ("There was an ERROR Loggin in. Try again"))
            return redirect('login')
    return render(request,'login.html',{'form':form,})





def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out"))
    return redirect('home')



def add_assignment(request):
    form = AssignmentForm(request.POST or None)
    if form.is_valid():
        assignment = form.save(commit=False)
        assignment.creator = request.user
        # assignment.post_time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
        assignment.save()
        return redirect('home')

    return render(request, 'addtask.html', {'form': form})


def view_submissions(request,id):
    assignment = Assignment.objects.get(pk=id)
    submissions = Submission.objects.filter(assignment=assignment)
    return render(request, 'view_submission.html', {'submissions' : submissions,'assignment':assignment})


def submit(request, id):
    form = SubmissionForm(request.POST or None)
    assignment = Assignment.objects.get(pk=id)
    if form.is_valid():
        submission = form.save(commit=False)
        submission.user = request.user
        submission.assignment = assignment
        # submission.time_submitted = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
        submission.save()
        return redirect('home')

    return render(request, 'register2.html', {'form': form, 'assignment':assignment})

def student_list(request):
    student_list = User.objects.all()
    return render(request, 'student_list.html', {'student_list':student_list})




def update_student(request,id):
    student = User.objects.get(pk=id)
    form = UpdateStudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()

        return redirect('student-list')
    return render(request, 'update_student.html', {'student' : student, 'form': form})

def delete_student(request,id):
    student = User.objects.get(pk=id)
    student.delete()
    return redirect('student-list')

def select_class(request):
    if request.method == 'POST':
        student_form = StudentRegistration(request.POST)
        if student_form.is_valid():
            student = student_form.save()
            messages.success(request, ("User Registered"))
            return redirect('login')
        else:
            messages.success(request, ("Form is invalid!"))
            return redirect('register')
    else:
        student_form = StudentRegistration()
        return render(request,'class.html',{'student_form':student_form}) 

def teacher_list(request):
    teacher_list = User.objects.all()
    return render(request, 'teacher_list.html', {'teacher_list':teacher_list})  

def update_teacher(request,id):
    teacher = User.objects.get(pk=id)
    form = UpdateUserForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('teacher-list')
    return render(request, 'update_teacher.html', {'teacher' : teacher, 'form': form}) 




def view_task_teacher(request):
    assignments = Assignment.objects.filter(creator=request.user)
    return render(request, 'view_task.html', {'assignments' : assignments})


def view_task_admin(request):
    assignments = Assignment.objects.all()
    return render(request, 'view_task.html', {'assignments' : assignments})


def view_task_student(request):
    assignments = Assignment.objects.filter(standard=request.user.standard)
    return render(request, 'view_task.html', {'assignments' : assignments})





# def add_task(request):
#     submitted=False
#     if request.method == "POST":
#         form = TeacherTaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/add_task?submitted=True')
#     else:
#         form = TeacherTaskForm
#         if 'submitted' in request.GET:
#             submitted = True
#         return render(request, 'addtask.html', {'form' : form, 'submitted':submitted})


# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('home')




# class TeacherSignUpView(CreateView):
#     model = User
#     form_class = TeacherSignUpForm
#     template_name = 'registration/signup_form.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'teacher'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('home')
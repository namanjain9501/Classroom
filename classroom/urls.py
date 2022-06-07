from django.urls import path, include
from . import views

urlpatterns = [
    # path('register_user', UserRegisterView.as_view(), name="register"),
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path('add_task/', views.add_assignment, name="add-task"),
    path('view_submission/<id>', views.view_submissions, name="view-submissions"),
    path('submit/<id>', views.submit, name="submit"),
    path('student_list', views.student_list, name="student-list"),
    path('update_student/<id>', views.update_student, name="update_student"),
    path('class', views.select_class, name="class"),
    path('delete_student/<id>', views.delete_student, name="delete-student"),
    path('teacher_list', views.teacher_list, name="teacher-list"),
    path('update_teacher/<id>', views.update_teacher, name="update-teacher"),
    path('add_student/', views.add_student, name="add_student"),
    path('add_teacher/', views.add_teacher, name="add_teacher"),
    path('view_task_student', views.view_task_student, name="view-task-student"),
    path('view_task_admin', views.view_task_admin, name="view-task-admin"),
    path('view_task_teacher', views.view_task_teacher, name="view-task-teacher"),
]


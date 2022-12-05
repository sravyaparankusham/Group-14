from django.urls import path

from . import views

urlpatterns = [
    
    path('home/', views.home, name = 'home'),
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('searchattendence/', views.searchAttendence, name='searchattendence'),
    path('account/', views.facultyProfile, name='account'),

    path('updateStudentRedirect/', views.updateStudentRedirect, name='updateStudentRedirect'),
    path('updateStudent/', views.updateStudent, name='updateStudent'),
    path('attendence/', views.takeAttendence, name='attendence'),
    path('delete/<Student_ID>', views.delete_attn, name='delete'),
   
]
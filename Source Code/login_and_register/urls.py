from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    # path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
    path('leaveform/', views.leaveform, name='leaveform'),
    path('dashboard_redirect_after_leave_apply/', views.dashboard_redirect_after_leave_apply, name='dashboard_redirect_after_leave_apply'),
    path('profile_page/', views.profile_page, name='profile_page'),
    # path('facultypage/', views.faculty, name='facultypage'),
    # path('ta/', views.ta, name='ta'),
    # path('student/', views.student, name='student'),
]   
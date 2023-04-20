from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout_view'),
    path('leaveform/', views.leaveform, name='leaveform'),
    path('dashboard_redirect_after_leave_apply/', views.dashboard_redirect_after_leave_apply,
         name='dashboard_redirect_after_leave_apply'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('admin_page', views.admin_page, name='admin_page'),
    # path('leave_status', views.leave_status, name='leave_status'),
    path('leave_status_pending', views.leave_status_pending,
         name='leave_status_pending'),
    path('leave_status_approved', views.leave_status_approved,
         name='leave_status_approved'),
    path('leave_status_rejected', views.leave_status_rejected,
         name='leave_status_rejected'),
    path('accept_leave', views.accept_leave, name='accept_leave'),
    path('reject_leave', views.reject_leave, name='reject_leave'),
    path('pending_to_approved/<str:oid>/',
         views.pending_to_approved, name='pending_to_approved'),  # when data is to be fetched from template to view function then we use <str:oid> and when data is to be fetched from view function to template then we use {{oid}}
         
         

]

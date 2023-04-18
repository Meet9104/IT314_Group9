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

]

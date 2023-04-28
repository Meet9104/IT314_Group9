from django.test import TestCase
from django.test import Client
from django.urls import reverse
from login_and_register.models import User
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.logout_view_url = reverse('logout_view')
        self.leaveform_url = reverse('leaveform')
        self.dashboard_redirect_after_leave_apply_url = reverse('dashboard_redirect_after_leave_apply')
        self.profile_page_url = reverse('profile_page')
        self.admin_page_url = reverse('admin_page')
        self.leave_status_pending_url = reverse('leave_status_pending')
        self.leave_status_approved_url = reverse('leave_status_approved')
        self.leave_status_rejected_url = reverse('leave_status_rejected')
        self.pending_to_approved_url = reverse('pending_to_approved',args=['some-str'])
        self.pending_to_rejected_url = reverse('pending_to_rejected',args=['some-str'])
        self.approved_to_rejected_url = reverse('approved_to_rejected',args=['some-str'])
        self.rejected_to_approved_url = reverse('rejected_to_approved',args=['some-str'])
        self.approved_leave_data_url = reverse('approved_leave_data')


    def test_index(self):
        response=self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'index.html')

    # def test_logout_view(self):
    #     response=self.client.get(self.logout_view_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'index.html')

    # def test_leaveform(self):
    #     response=self.client.get(self.leaveform_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'leaveform.html')

    
    # def test_dashboard_redirect_after_leave_apply(self):
    #     response=self.client.get(self.dashboard_redirect_after_leave_apply_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'leaveform.html')

    # def test_profile_page(self):
    #     response=self.client.get(self.profile_page_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'index.html')

    # def test_admin_page(self):
    #     response=self.client.get(self.admin_page_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'admin_page.html')

    # def test_leave_status_pending(self):
    #     response=self.client.get(self.leave_status_pending_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'leave_status_pending.html')

    # def test_leave_status_approved(self):
    #     response=self.client.get(self.leave_status_approved_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'leave_status_approved.html')

    # def test_leave_status_rejected(self):
    #     response=self.client.get(self.leave_status_rejected_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'leave_status_rejected.html')
    
    # def test_pending_to_approved(self):
    #     response=self.client.get(self.pending_to_approved_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'pending_to_approved.html')

    # def test_pending_to_rejected(self):
    #     response=self.client.get(self.pending_to_rejected_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'pending_to_rejected.html')
        
    # def test_approved_to_rejected(self):
    #     response=self.client.get(self.approved_to_rejected_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'approved_to_rejected.html')

    # def rejected_to_approved(self):
    #     response=self.client.get(self.rejected_to_approved_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'leave_status_rejected.html')

    # def test_approved_leave_data(self):
    #     response=self.client.get(self.approved_leave_data_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'leave_status_approved.html')












    
    




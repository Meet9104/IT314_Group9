from django.test import SimpleTestCase
from django.urls import reverse
from django.urls import resolve

from login_and_register.views import logout_view
from login_and_register.views import index
from login_and_register.views import leaveform
from login_and_register.views import dashboard_redirect_after_leave_apply
from login_and_register.views import profile_page
from login_and_register.views import admin_page
from login_and_register.views import leave_status_pending
from login_and_register.views import leave_status_approved
from login_and_register.views import leave_status_rejected
from login_and_register.views import pending_to_approved
from login_and_register.views import pending_to_rejected
from login_and_register.views import approved_to_rejected
from login_and_register.views import rejected_to_approved
from login_and_register.views import approved_leave_data



class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url=reverse('index')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,index)

    def test_logout_view(self):
        url=reverse('logout_view')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,logout_view)

    def test_leaveform(self):
        url=reverse('leaveform')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,leaveform)

    def test_dashboard_redirect_after_leave_apply(self):
        url=reverse('dashboard_redirect_after_leave_apply')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,dashboard_redirect_after_leave_apply)

    def test_profile_page(self):
        url=reverse('profile_page')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,profile_page)

    def test_admin_page(self):
        url=reverse('admin_page')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,admin_page)

    def test_leave_status_pending(self):
        url=reverse('leave_status_pending')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,leave_status_pending)

    def test_leave_status_approved(self):
        url=reverse('leave_status_approved')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,leave_status_approved)

    def test_leave_status_rejected(self):
        url=reverse('leave_status_rejected')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,leave_status_rejected)

    def test_pending_to_approved(self):
        url=reverse('pending_to_approved',args=['some-str'])
        # print(resolve(url))
        self.assertEquals(resolve(url).func,pending_to_approved)

    def test_pending_to_rejected(self):
        url=reverse('pending_to_rejected',args=['some-str'])
        # print(resolve(url))
        self.assertEquals(resolve(url).func,pending_to_rejected)

    def test_approved_to_rejected(self):
        url=reverse('approved_to_rejected',args=['some-str'])
        # print(resolve(url))
        self.assertEquals(resolve(url).func,approved_to_rejected)
    
    def test_rejected_to_approved(self):
        url=reverse('rejected_to_approved',args=['some-str'])
        # print(resolve(url))
        self.assertEquals(resolve(url).func,rejected_to_approved)

    def test_approved_leave_data(self):
        url=reverse('approved_leave_data')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,approved_leave_data)

    












































    
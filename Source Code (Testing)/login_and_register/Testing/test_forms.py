from django.test import SimpleTestCase
from login_and_register.forms import LoginForm


class TestForms(SimpleTestCase):

    def test_Login_form_valid_data(self):
        # Creating an instance of the LoginForm with valid data
        form=LoginForm(data={
            'username':'harsh@gmail.com',
            'password':'harsh'
        }) 

        # Asserting that the form is valid
        self.assertTrue(form.is_valid())

    def test_Login_form_invalid_pass(self):
        # Creating an instance of the LoginForm with invalid password
        form=LoginForm(data={
            'username':'darshan@gmail.com',
            'password':''
        }) 

        # Asserting that the form is not valid
        self.assertFalse(form.is_valid())

    def test_Login_form_invalid_mail(self):
        # Creating an instance of the LoginForm with invalid mail ID
        form=LoginForm(data={
            'username':'',
            'password':'pwd'
        }) 

        # Asserting that the form is not valid
        self.assertFalse(form.is_valid())

    def test_Login_form_invalid_data(self):
        # Creating an instance of the LoginForm with invalid data
        form=LoginForm(data={
            'username':'',
            'password':''
        }) 

        # Asserting that the form is not valid
        self.assertFalse(form.is_valid())

    

        


















































        
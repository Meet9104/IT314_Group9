from django.test import TestCase
from login_and_register.models import User

class UserModelTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            email='user@gmail.com',
            password='password'
        )
    
    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.__str__(), self.user.username)
    
    def test_user_type(self):
        self.assertFalse(self.user.is_faculty)
        self.assertFalse(self.user.is_ta)
        self.assertFalse(self.user.is_student)
        
        self.user.is_faculty = True
        self.user.save()
        self.assertTrue(self.user.is_faculty)
        
        self.user.is_ta = True
        self.user.save()
        self.assertTrue(self.user.is_ta)
        
        self.user.is_student = True
        self.user.save()
        self.assertTrue(self.user.is_student)
        
        self.user.is_faculty = False
        self.user.save()
        self.assertFalse(self.user.is_faculty)
        
        self.user.is_ta = False
        self.user.save()
        self.assertFalse(self.user.is_ta)
        
        self.user.is_student = False
        self.user.save()
        self.assertFalse(self.user.is_student)






































from django.test import TestCase,RequestFactory
from .models import User,Profile
from . import views as reg_views
from ..faculty import views as fac_views
from django.urls import reverse

class User_ModelTest(TestCase):
	def createUser(self,first_name='Testname',last_name='last',password='Checkpasswd',email='gywg@gmail.com',u_type='faculty'):
		return User.objects.create(first_name='Testname',last_name='last',password='Checkpasswd',email='gywg@gmail.com',u_type='faculty')
	def test_user_creation(self):
		w = self.createUser()
		self.assertTrue(isinstance(w, User))
		self.assertEqual(w.__unicode__(), w.email)
		#self.assertLess()

class UserManagerTest(TestCase):
	def createUser(self,first_name='Testname',last_name='last',password='Checkpasswd',email='gywg@gmail.com',u_type='faculty'):
		return User.objects.create(first_name='Testname',last_name='last',password='Checkpasswd',email='gywg@gmail.com',u_type='faculty')
	def test_userManager_creation(self):
		w = self.createUser()
		self.assertEqual(w.first_name.isalpha() , True)
		self.assertEqual(w.last_name.isalpha() , True)
		self.assertGreater(len(w.password),8)
		self.assertNotEqual(len(w.last_name), 0)

class BlackBoxtesting(TestCase):
	def setUp(self):
		self.factory=RequestFactory()
		self.User = User.objects.create(first_name='Testname',last_name='last',password='Checkpasswd',email='gywg@gmail.com',u_type='hod')
	
	def test_redirect(self):
		request = self.factory.get('/faculty/')
		request.User = self.User
		#request.session['id'] = self.User.email
		response = fac_views.faculty(request)
		self.assertEqual(response.status_code, 200)

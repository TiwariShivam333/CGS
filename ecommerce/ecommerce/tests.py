from django.test import TestCase

class test_urls(TestCase):
	def test_register(self):
		url = reverse('register')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)



	def test_login_user(self):
		url = reverse('login')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)

	def test_cart(self):
		url = reverse('cart')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)

	def test_order(self):
		url = reverse('order')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)

	def test_shop(self):
		url = reverse('shop')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)

# from django.test import TestCase
# from django.contrib.auth import get_user_model

# # Create your tests here.

# class MoelTests(TestCase):
#     """Test for models"""

#     def test_create_user_login_successful(self):
#         """Test to create user credentials is successful"""
#         email = 'test@example.com'
#         password = 'test@123'
#         user = get_user_model().objects.create_user(email=email, password=password)

#         self.assert_Equal(user.email, email)
#         self.assertTrue(user.check_password(password))


#     def test_new_user_email_normalized(self):
#         """Test, email is normalized for new users"""
#         sample_email = [
#             ['test1@EXAMPLE.com', 'test1@example.com'],
#             ['Test2@Example.com', 'Test2@example.com'],
#             ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
#         ]
#         for email, expected in sample_email:
#             user = get_user_model().objects.create_user(email, 'sample123')
#             self.assertEqual(user.email, expected)

#         def test_user_without_email_raises_error(self):
#             """Test that creating a user without email raises a ValueError"""
#             with self.assertRaises(ValueError):
#                 get_user_model().onbjects.create_user('', 'test123')
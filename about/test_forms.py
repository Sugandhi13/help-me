# Importing required libraries to test the forms

from django.test import TestCase
from .forms import ContactForm, UserProfileForm

# Created TestContactForm class to run test scenarios for contact form
class TestContacteForm(TestCase):

    # TestCase1 : Testing when all valid inputs were given then form works as expected 
    def test_form_is_valid(self):
        """ Test for all fields"""
        form = ContactForm({
            'name': 'Test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    # TestCase2 : Testing when name field is missing then form should fail 
    def test_form_have_invalid_name(self):
        """ Test for all fields"""
        form = ContactForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Name field is not valid, but the Form is valid")

    # TestCase3 : Testing when email field is entered incorrect then form should fail
    def test_form_have_invalid_email(self):
        """ Test for all fields"""
        form = ContactForm({
            'name': 'Test',
            'email': 'emailtest',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Email field is not valid, but the Form is valid")

    # TestCase4 : Testing when message field is missing then form should fail
    def test_form_have_invalid_message(self):
        """ Test for all fields"""
        form = ContactForm({
            'name': 'Test',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(), msg="Message field is not valid, but the Form is valid")


# Created TestUserProfileForm class to run test scenarios for user profile form
class TestUserProfileForm(TestCase):

    # TestCase1 : Testing when all valid inputs were given then form works as expected 
    def test_form_is_valid(self):
        """ Test for all fields"""
        form = UserProfileForm({
            'first_name': 'Firstname', 
            'last_name': 'Lastname', 
            'email': 'test@email.com', 
            'profile_image': 'xyx.jpg', 
            'describe_yourself': 'This is a test profile'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    # TestCase2 : Testing when firstname field is missing then form should fail
    def test_form_have_invalid_firstname(self):
        """ Test for all fields"""
        form = ContactForm({
            'first_name': '', 
            'last_name': 'Lastname', 
            'email': 'test@email.com', 
            'profile_image': 'xyx.jpg', 
            'describe_yourself': 'This is a test profile'
        })
        self.assertFalse(form.is_valid(), msg="First name field is not valid, but the Form is valid")

    # TestCase3 : Testing when lastname field is missing then form should fail
    def test_form_have_invalid_lastname(self):
        """ Test for all fields"""
        form = ContactForm({
            'first_name': 'Firstname', 
            'last_name': '', 
            'email': 'test@email.com', 
            'profile_image': 'xyx.jpg', 
            'describe_yourself': 'This is a test profile'
        })
        self.assertFalse(form.is_valid(), msg="Last name field is not valid, but the Form is valid")

    # TestCase4 : Testing when email field is missing then form should fail
    def test_form_have_invalid_email(self):
        """ Test for all fields"""
        form = ContactForm({
            'first_name': 'Firstname', 
            'last_name': 'Lastname', 
            'email': '', 
            'profile_image': 'xyx.jpg', 
            'describe_yourself': 'This is a test profile'
        })
        self.assertFalse(form.is_valid(), msg="Email field is not valid, but the Form is valid")

    # TestCase5 : Testing when describe yourself field is missing then form should fail
    def test_form_have_invalid_describe(self):
        """ Test for all fields"""
        form = ContactForm({
            'first_name': 'Firstname', 
            'last_name': 'Lastname', 
            'email': 'test@email.com',
            'profile_image': 'xyx.jpg', 
            'describe_yourself': ''
        })
        self.assertFalse(form.is_valid(), msg="Describe yourself field is not valid, but the Form is valid")

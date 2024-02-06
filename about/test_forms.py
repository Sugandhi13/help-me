from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_have_valid_name(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Name field is not valid, but the Form is valid")

    def test_form_have_valid_email(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Test',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Email field is not valid, but the Form is valid")

    def test_form_have_valid_message(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Test',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(), msg="Message field is not valid, but the Form is valid")

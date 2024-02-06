from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutViews(TestCase):

    def setUp(self):
        self.about = About(title="About title", content="About content")
        self.about.save()

    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
    
    def test_successful_collaborate_submission(self):
        """Test for posting a collaboration message"""

        collaborate_data = {
            'name': 'Test',
            'email': 'test@test.com',
            'message': 'Request to collaborate'
        }
        response = self.client.post(reverse('about'), collaborate_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )

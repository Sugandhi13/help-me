from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import AnswerForm
from .models import Query


class TestQueryViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.query = Query(title="Query title", author=self.user,
                         slug="query-title", excerpt="Query excerpt",
                           content="Query content", status=1)
        self.query.save()

    def test_render_query_detail_page_with_answer_form(self):
        response = self.client.get(reverse(
            'query_detail', args=['query-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Query title", response.content)
        self.assertIn(b"Query content", response.content)
        self.assertIsInstance(
            response.context['answer_form'], AnswerForm)

    def test_successful_answer_submission(self):
        """Test for posting an answer on a query"""
        self.client.login(
            username="myUsername", password="myPassword")
        answer_data = {
            'query_answer': 'This is a test answer.'
        }
        response = self.client.post(reverse(
            'query_detail', args=['query-title']), answer_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Answer submitted and awaiting approval',
            response.content
        )

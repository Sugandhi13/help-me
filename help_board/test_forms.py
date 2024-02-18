from django.test import TestCase
from .forms import QueryForm, AnswerForm


class Testanswerform(TestCase):


    def test_form_is_valid(self):
        answer_form = AnswerForm({'content': 'This is a great post'})
        self.assertTrue(answer_form.is_valid(), msg_prefix='Form is valid')

    def test_form_is_invalid(self):
        answer_form = AnswerForm({'content': ''})
        self.assertFalse(answer_form.is_valid(), msg_prefix='Form is not valid')


class Testquery_form(TestCase):

    def test_form_is_valid(self):
        query_form = QueryForm(
            {
                'title': 'This is a title', 
                'category': 'Travel',
                'content': 'This is a great post'
            }
        )
        self.assertTrue(query_form.is_valid(), msg='Query form is valid')

    def test_form_have_invalid_name(self):
        query_form = QueryForm(
            {
                'title': '', 
                'category': 'Travel',
                'content': 'This is a great post'
            }
        )
        self.assertFalse(query_form.is_valid(), msg='Query title can not be empty, but the Form is valid')

    def test_form_have_invalid_category(self):
        query_form = QueryForm(
            {
                'title': 'This is a title', 
                'category': '',
                'content': 'This is a great post'
            }
        )
        self.assertFalse(query_form.is_valid(), msg='Query category can not be empty, but the Form is valid')

    def test_form_have_invalid_category_entered(self):
        query_form = QueryForm(
            {
                'title': 'This is a title', 
                'category': 'Random',
                'content': 'This is a great post'
            }
        )
        self.assertFalse(query_form.is_valid(), msg='Random category is invalid, but the Form is valid')

    def test_form_have_invalid_content(self):
        query_form = QueryForm(
            {
                'title': 'This is a title', 
                'category': 'Travel',
                'content': ''
            }
        )
        self.assertFalse(query_form.is_valid(), msg='Query Content can not be empty, but the Form is valid')



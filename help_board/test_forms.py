# Importing required libraries to test the forms

from django.test import TestCase
from .forms import QueryForm, AnswerForm


# Created TestAnswerForm class to run test scenarios for answer form
class TestAnswerForm(TestCase):

    # TestCase1 : Testing when all valid inputs given then form works fine
    def test_form_is_valid(self):
        answer_form = AnswerForm({'content': 'This is a great post'})
        self.assertTrue(
            answer_form.is_valid(), msg='Form is invalid'
        )

    # TestCase2 : Testing when content field is missing then form should fail
    def test_form_is_invalid(self):
        answer_form = AnswerForm({'content': ''})
        self.assertFalse(
            answer_form.is_valid(), msg='Content invalid but form is valid'
        )


# Created TestQueryForm class to run test scenarios for query form
class TestQueryForm(TestCase):

    # TestCase1 : Testing when title field is missing then form should fail
    def test_form_have_invalid_name(self):
        query_form = QueryForm(
            {
                'title': '',
                'category': 'Travel',
                'content': 'This is a great post'
            }
        )
        self.assertFalse(
            query_form.is_valid(), msg='Query title invalid, but form is valid'
        )

    # TestCase2 : Testing when category field is missing then form should fail
    def test_form_have_invalid_category(self):
        query_form = QueryForm(
            {
                'title': 'This is a title',
                'category': '',
                'content': 'This is a great post'
            }
        )
        self.assertFalse(
            query_form.is_valid(), msg='Query category invalid, form is valid'
        )

    # TestCase3 : Testing when incorrect category added then form should fail
    def test_form_have_invalid_category_entered(self):
        query_form = QueryForm(
            {
                'title': 'This is a title',
                'category': 'Random',
                'content': 'This is a great post'
            }
        )
        self.assertFalse(
            query_form.is_valid(), msg='Random category invalid, form is valid'
        )

    # TestCase4 : Testing when content field is missing then form should fail
    def test_form_have_invalid_content(self):
        query_form = QueryForm(
            {
                'title': 'This is a title',
                'category': 'Travel',
                'content': ''
            }
        )
        self.assertFalse(
            query_form.is_valid(), msg='Query Content invalid, form is valid'
        )

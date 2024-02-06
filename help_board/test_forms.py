from django.test import TestCase
from .forms import AnswerForm


class Testanswer_form(TestCase):

    def test_form_is_valid(self):
        answer_form = AnswerForm({'query_answer': 'This is a great post'})
        self.assertTrue(answer_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        answer_form = AnswerForm({'query_answer': ''})
        self.assertFalse(answer_form.is_valid(), msg='Form is valid')

from django.test import TestCase
from blog.forms import CommentForm
from django.utils import timezone
from datetime import datetime

class CommentFormTest(TestCase):
    
    # @classmethod
    # def setUpTestData(cls):
    
    def test_form_submission_date(self):
        form = CommentForm(
            data={
                "name": "Commenter",
                "email": "commenter@blog.com",
                "body": "Testing comment submission",
            }
        )
        form1 = CommentForm(
            data={
                "email": "commenter@blog.com",
                "body": "Testing comment submission",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertFalse(form1.is_valid())
        
    def test_form_date_timezone(self):
        form = CommentForm(
            data={
                "name": "Commenter",
                "email": "commenter@blog.com",
                "body": "Testing comment submission",
                "created": datetime.now(),
            }
        )
        self.assertTrue(form.is_valid())
        
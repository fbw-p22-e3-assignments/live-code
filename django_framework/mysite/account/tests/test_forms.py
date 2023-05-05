from django.test import TestCase
from account.forms import UserRegistrationForm
from django import forms

class UserRegistrationFormTest(TestCase):
    
    def test_form_widgets(self):
        form = UserRegistrationForm()
        widget = form['password'].as_widget()
        self.assertTrue(widget, forms.PasswordInput())
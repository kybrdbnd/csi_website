__author__ = 'kybrdbnd'

from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, error_messages={
                                 'required': 'Please enter your name'})
    phone = forms.DecimalField(required=False, max_digits=10)
    sender = forms.EmailField(required=True, error_messages={
                              'required': 'Please enter your email id'})
    message = forms.CharField(required=True, error_messages={
                              'required': 'Please enter your message'})
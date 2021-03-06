"""This file defines all the forms in exam app"""

from django import forms
from django.forms.formsets import BaseFormSet

ANSWER_CHOICES = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))


class BaseAnswerFormSet(BaseFormSet):
    """BaseAnswerFormSet() cleans the data in the form"""
    def clean(self):
        so = []
        for i in range(0, self.total_form_count()):
            form = self.forms[i]
            try:
                so.append(form.cleaned_data['options'])
            except KeyError:
                so.append('X')
        return so


class AnswerForm(forms.Form):
    """AnswerForm is a template for Options to a question"""
    options = forms.ChoiceField(choices=ANSWER_CHOICES,
                                 widget=forms.RadioSelect())

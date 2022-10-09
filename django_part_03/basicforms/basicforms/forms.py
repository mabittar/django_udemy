from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(validators=[validators.EmailValidator])
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcacher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name or len(name) <= 1:
            raise forms.ValidationError("Invalid Name!")
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        if not self.cleaned_data.get('email'):
            raise forms.ValidationError('Informe seu e-mail ou telefone.', code='phone_or_email')

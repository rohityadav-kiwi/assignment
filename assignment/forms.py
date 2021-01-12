from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from assignment.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(required=True)
    bio = forms.CharField(max_length=10000, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        """save method"""
        # Save the provided password in hashed format
        user = super(SignUpForm, self).save(commit=False)
        user.save()
        user_profile = Profile(user=user, birth_date=self.cleaned_data['birth_date'], bio=self.cleaned_data['bio'])
        user.save()
        user_profile.save()
        return user, user_profile


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

def validate_password(password, user=None, password_validators=None):
    """
    Validate whether the password meets all validator requirements.

    If the password is valid, return ``None``.
    If the password is invalid, raise ValidationError with all error messages.
    """
    errors = []
    if password_validators is None:
        password_validators = password_validation.get_default_password_validators()
    for validator in password_validators:
        try:
            validator.validate(password, user)
        except ValidationError as error:
            errors.append(error)
    if errors:
        raise ValidationError(errors[0])

class SignupForm(forms.ModelForm):
    password = forms.CharField(
        #label="Password"),
        strip=False,
        widget=forms.TextInput(attrs={'placeholder': 'Password*'}),
        #widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        #help_text=password_validation.password_validators_help_text_html(),
    )
    class Meta:
      model = User
      fields = ('password',)
  
    def _post_clean(self):
        password = self.cleaned_data.get('password')
        if password:
            try:
              validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password', error)
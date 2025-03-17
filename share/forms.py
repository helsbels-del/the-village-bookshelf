from django import forms
from .models import Books
from django.core.validators import MinLengthValidator, RegexValidator 


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["title", "author", "genre", "description"]
     

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)  
    email = forms.EmailField()  
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            MinLengthValidator(8),  # Minimum length of 8 characters
            RegexValidator(r'.*\d', 'Password must contain at least one number.'),
            RegexValidator(r'.*[A-Z]', 'Password must contain at least one uppercase letter.'),
            RegexValidator(r'.*[a-z]', 'Password must contain at least one lowercase letter.'),
            RegexValidator(r'.*[@$!%*?&]', 'Password must contain at least one special character (@, $, !, %, *, ?, &).'),
        ]
    )
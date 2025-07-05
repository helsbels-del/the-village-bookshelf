from django import forms
from .models import Books
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title', 'author', 'description', 'condition', 'genre', 'available']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  
 
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
 
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email  # Return the cleaned email
 
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user  


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'autocorrect': 'off',
            'autocapitalize': 'none',
            'spellcheck': 'false',
            'placeholder': 'Username',
            'name': 'login-username',  # use a "weird" name
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'placeholder': 'Password',
            'name': 'login-password',  # use a "weird" name
        })
    )





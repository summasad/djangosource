from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    # 이메일 필수입력 처리
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username","email")
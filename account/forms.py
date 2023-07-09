from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','phone_no','password1','password2']
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

        model = get_user_model
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):

        model = get_user_model
        fields = ('email', 'username')
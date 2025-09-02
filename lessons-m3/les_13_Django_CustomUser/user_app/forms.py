from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации нового пользователя нва основе кастомной модели."""
    email = forms.EmailField(
        required=True,
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )

    class Meta:
        model = get_user_model()
        fields = ('email', )

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email уже  зарегистрирован')
        return email
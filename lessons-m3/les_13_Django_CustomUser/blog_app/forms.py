from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите контент'}),
    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=10,
        label='Рейтинг',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )


class PostModelForm(forms.ModelForm):
    """Форма для создания постов на основе модели."""
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'rating', 'tags')
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'author': 'Автор',
            'rating': 'Рейтинг',
            'tags': 'Тэги'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите контент'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Заголовок должен быть не менее 5 символов')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 10:
            raise ValidationError('Контент должен быть не менее 10 символов')
        return content

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        forbidden_words = ['казино', 'крипта']

        if content:
            for word in forbidden_words:
                if word in content.lower():
                    raise ValidationError(f'Текст не должен содержать запрещенное слово {word}')

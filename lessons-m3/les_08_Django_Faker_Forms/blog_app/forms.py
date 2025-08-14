from django import forms
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
import pytest
from blog_app.models import Post, Author, Tag
from blog_app.forms import PostForm, PostModelForm


@pytest.mark.django_db
def test_post_form_validation():
    """Проверка валидации PostForm."""
    form_data = {
        'title': 'Тестовый пост',
        'content': 'Это содержимое тестового поста',
        'rating': 5,
    }
    form = PostForm(data=form_data)

    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['title'] == form_data['title']
    assert cleaned_data['rating'] == 5
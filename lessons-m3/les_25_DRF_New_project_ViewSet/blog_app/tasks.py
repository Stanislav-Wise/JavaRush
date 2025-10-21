from celery import shared_task
import time
from django.core.mail import send_mail
from .models import Post


@shared_task
def add(x, y):
    time.sleep(3)
    return x + y


@shared_task
def send_notification_email(recipient_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='megamozg137@mail.ru',
        recipient_list=[recipient_email],
    )
    return f'Почта отправлена на {recipient_email}'


@shared_task
def add_post_rating():
    """Периодичкская задача по увеличению рейтинга постов."""
    posts = Post.objects.all()
    for post in posts:
        post.rating += 1
        post.save()
    return f'Обновлено {posts.count()} постов'
from celery import shared_task
import time
from django.core.mail import send_mail


@shared_task
def add(x, y):
    time.sleep(3)
    return x + y


@shared_task
def send_notification_email(recipient_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@admin.ru',
        recipient_list=[recipient_email],
    )
    return f'Почта отправлена на {recipient_email}'

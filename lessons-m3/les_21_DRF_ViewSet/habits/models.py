from django.db import models
from django.conf import settings


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name='Пользователь',
    )

    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reward_to',
        verbose_name='связанная привычка',
        help_text='Укажите приятную привычку',
    )

    place = models.CharField(
        max_length=255,
        verbose_name='Место',
        help_text='Где выполняется привычка',
    )

    time = models.TimeField(
        verbose_name='Время выполнения',
        help_text='Во сколько выполнять'
    )

    action = models.CharField(
        max_length=255,
        verbose_name='Действие',
        help_text='Что будете делать',
    )

    is_public = models.BooleanField(
        default=False,
        verbose_name='Публичная или нет'
    )

    is_pleasent = models.BooleanField(
        default=False,
        verbose_name='Приятная привычка?',
    )

    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Периодичность (дней)'
    )

    reward = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Вознаграждение',
    )

    duration = models.PositiveSmallIntegerField(
        default=60,
        verbose_name='Длительность (сек)',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создана',
    )

    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Обновлена',
    )

    def __str__(self):
        return f'[user={self.user}] {self.place} -> {self.action} @ {self.time}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['-created_at']

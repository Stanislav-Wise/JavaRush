from rest_framework import serializers
from habits.models import Habit


class HabitRelatedSerializer(serializers.ModelSerializer):
    """Мини-сериализатор для вывода связанной привычки."""

    class Meta:
        model = Habit
        fields = [
            'id',
            'action',
            'is_pleasent',
            'time',
            'place',
        ]
        read_only_fields = fields


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для полноценного CRUD по Habits + вычисляемые поля."""

    time_hhmm = serializers.SerializerMethodField(read_only=True)

    related_habit_action = serializers.SerializerMethodField(read_only=True)

    duration_minutes = serializers.SerializerMethodField(read_only=True)

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    related_habit_info = HabitRelatedSerializer(
        source='related_habit',
        read_only=True,
    )

    class Meta:
        model = Habit
        fields = [
            'id',
            'user',
            'action',
            'place',
            'time',
            'is_public',
            'is_pleasent',
            'periodicity',
            'reward',
            'duration',
            'created_at',
            'updated_at',
            'related_habit',

            # Новые вычисляемые поля
            'time_hhmm',
            'related_habit_action',
            'duration_minutes',

            # Новые вложенное поля
            'related_habit_info',

        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'action': {
                'trim_whitespace': True  # Если было "  Бег  ", то станет "Бег"
            },
            'place': {
                'trim_whitespace': True  # Если было "  Бег  ", то станет "Бег"
            },
            'reward': {
                'required': False,  # Клинет может не присылать это поле
                'allow_null': True,  # Клинет может присылать null
                'allow_blank': False,  # Клинет может присылать пустую строку
            },
            'related_habit': {
                'required': False,  # Клинет может не присылать это поле
                'allow_null': True,  # Клинет может присылать null
            },
        }

    def get_time_hhmm(self, obj):
        t = obj.time
        return t.strftime('%H:%M') if t else None

    def get_related_habit_action(self, obj):
        rh = obj.related_habit
        return rh.action if rh else None

    def get_duration_minutes(self, obj):
        seconds = obj.duration
        if seconds is None:
            return None
        return seconds // 60





    #
    # related_habit
    # place
    # time
    # action
    # is_public
    # is_pleasent
    # periodicity
    # reward
    # duration =
    # created_at
    # updated_at
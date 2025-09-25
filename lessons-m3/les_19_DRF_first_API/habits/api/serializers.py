from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

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
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]
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
from django.contrib import admin
from .models import Habit
# Register your models here.


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    pass
# Точка входа для запуска Celery-воркера
from app.tasks import celery_app

# команда для запуска celery -  celery -A celery_worker.celery_app worker -l INFO
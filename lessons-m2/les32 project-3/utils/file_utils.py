from pathlib import Path
import uuid


ALLOW_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif"]
MAX_FILE_SIZE = 5 * 1024 * 1024


def is_allowed_file(filename: Path) -> bool:
    """Проверяем, есть ли расширение в списке разрешенных."""
    # ext = filename.split(".")[-1]
    # file_path = Path(filename)
    ext = filename.suffix.lower()
    print(ext)
    return ext in ALLOW_EXTENSIONS


def get_unique_name(filename: Path) -> str:
    ext = filename.suffix.lower()
    unique_name = f"{uuid.uuid4().hex}{ext}"
    print(f"{unique_name=}")
    return unique_name
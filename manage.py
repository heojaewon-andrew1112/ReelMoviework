import os
import sys
import django
from django.core.management import execute_from_command_line


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongodbconnect.settings')  # 여기에서 settings 모듈을 명확히 설정
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mongodbconnect.settings")  # settings 모듈 설정 수정
    django.setup()
    execute_from_command_line(sys.argv)

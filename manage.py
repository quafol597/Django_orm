"""
manage.py文件用于迁移数据库: makemigrations and migrate
"""
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

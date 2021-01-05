"""
main.py文件用于数据库CRUD
"""
# ======================这是固定的配置==============================
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
application = get_wsgi_application()

from app.models import *
# =================================================================

# main函数用于编写数据库CURD
def main():
    pass


if __name__ == '__main__':

    main()

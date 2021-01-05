"""
settings.py文件主要用于配置数据库
"""
# test_seco
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'seco',
#         'USER': 'postgres',
#         'PASSWORD': 'xiaoan123',
#         'HOST': '10.10.0.197',
#         'PORT': 5432,
#         'OPTIONS': {'options': '-c search_path=seco'},  # 连接PG数据库指定模式 - seco
#     }
# }


# cloud_demo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'demo',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '8.129.49.94',
        'PORT': 5432,
        'OPTIONS': {'options': '-c search_path=orm'},
    }
}


# 这两个配置不需要修改
INSTALLED_APPS = [
    'app',
]
SECRET_KEY = 'replace_me'
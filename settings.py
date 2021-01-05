"""
settings.py文件主要用于配置数据库
"""
# ======================这是固定的配置==============================
INSTALLED_APPS = [
    'app',
]
SECRET_KEY = 'replace_me'
# =================================================================

# 下面为链接不同数据库的配置

# test_seco
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'seco',  # 数据库
#         'USER': 'postgres',  # 用户
#         'PASSWORD': 'xiaoan123',  # 密码
#         'HOST': '10.10.0.197',  # IP
#         'PORT': 5432,  # PORT
#         'OPTIONS': {'options': '-c search_path=seco'},  # Schema
#     }
# }


# cloud_demo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'demo',  # 数据库
        'USER': 'postgres',  # 用户
        'PASSWORD': 'postgres',  # 密码
        'HOST': '8.129.49.94',  # IP
        'PORT': 5432,  # PORT
        'OPTIONS': {'options': '-c search_path=orm'},  # Schema
    }
}

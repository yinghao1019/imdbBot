from .base import *
import dj_database_url

DEBUG=False
STATIC_ROOT='staticfiles'

# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES={
    "default":dj_database_url.config(ssl_require=True,conn_max_age=0)
}

os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', os.path.join(BASE_DIR,"imdbservice-credentials.json"))
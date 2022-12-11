"""
WSGI config for stock_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

# add the hellodjango project path into the sys.path
sys.path.append('/srv/stock_api')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_api.settings')

application = get_wsgi_application()

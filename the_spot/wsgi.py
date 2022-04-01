"""
WSGI config for the_spot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_spot.settings')

application = get_wsgi_application()

application = WhiteNoise(application, root="/path/to/static/files")
application.add_files("/path/to/more/static/files", prefix="more-files/")
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prompt.settings")

# from whitenoise.django import DjangoWhiteNoise

# application = DjangoWhiteNoise(get_wsgi_application())
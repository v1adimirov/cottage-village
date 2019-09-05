import os
from django.conf import settings

USE_ADMIN_AREA_TINYMCE = getattr(settings, "FLATPAGES_TINYMCE_ADMIN", True)
USE_FRONTED_TINYMCE = getattr(settings, "FLATPAGES_TINYMCE_FRONTEND", True)

USE_TEMPLATE_DROPDOWN = getattr(settings, "FLATPAGES_USE_TEMPLATE_DROPDOWN", True)
TEMPLATE_DIR = os.path.join(settings.BASE_DIR, 'project/templates/pages')
TEMPLATE_FILES_REGEXP = getattr(settings, 'FLATPAGES_ADMIN_REGEXP', r'.*\.d?html?')

DIV_PREFIX = getattr(settings, 'FLATPAGES_DIV_PREFIX', "django_staticpages_edit")

USE_MINIFIED = getattr(settings, 'FLATPAGES_USE_MINIFIED', None)
if USE_MINIFIED is None:
    USE_MINIFIED = not getattr(settings, 'DEBUG')

if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    MEDIA_URL = os.path.join(getattr(settings, 'STATIC_URL', ''), 'flatpages_tinymce')
else:
    MEDIA_URL = getattr(settings, 'FLATPAGES_MEDIA_URL', os.path.join(settings.MEDIA_URL, 'flatpages_tinymce'))

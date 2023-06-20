from django.conf import settings

def global_settings(request):
    # Return any necessary values or settings
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_LOGO': settings.SITE_LOGO,
        'COPYRIGHT_TEXT': settings.COPYRIGHT_TEXT,
    }

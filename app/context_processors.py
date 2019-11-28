from django.conf import settings


def settings_context(request):
    return {
        'APP_NAME': settings.APP_NAME,
    }

USE_DEBUG_TOOLBAR = True
if USE_DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES += \
        ('debug_toolbar.middleware.DebugToolbarMiddleware',)

    INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = (
    '10.2.2.2',
    )

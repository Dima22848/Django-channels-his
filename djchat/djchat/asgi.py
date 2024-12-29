import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from corsheaders.middleware import CorsMiddleware
from channels.auth import AuthMiddlewareStack
from . import urls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djchat.settings")

django_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": CorsMiddleware(django_application),  # Оборачиваем Django приложение в CORS middleware
        "websocket": AuthMiddlewareStack(
            URLRouter(urls.websocket_urlpatterns)
        ),
    }
)
























# import os

# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djchat.settings")

# django_application = get_asgi_application()

# from . import urls  # noqa isort:skip

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": URLRouter(urls.websocket_urlpatterns),
#     }
# )

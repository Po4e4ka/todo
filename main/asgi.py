import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
import main.socket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJANGO.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': application,
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws', main.socket.Consumer.as_asgi())
        ])
    )
})
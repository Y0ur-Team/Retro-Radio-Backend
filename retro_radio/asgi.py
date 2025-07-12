import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

# Set settings module BEFORE setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'retro_radio.settings')
django.setup() # hot fix as it hsould be loaded before importing routings i.e. down bellow : )
import core.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(core.routing.websocket_urlpatterns),
})

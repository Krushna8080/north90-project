# chat_project/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routing

# Add these lines before any other Django imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')
django_asgi_app = get_asgi_application()
# yourapp/templatetags/form_tags.py
from django import template
register = template.Library()

@register.filter(name='addclass')
def addclass(field, css):
    return field.as_widget(attrs={"class": css})

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
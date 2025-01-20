from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.chat_view, name='chat'),                           # Default route for chat
    path('chat/<int:user_id>/', views.chat_view, name='chat_with_user'),  # Chat with a specific user
    path('register/', views.register_view, name='register'),          # Registration page
    path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(next_page='/login'), name='logout'),  # Logout page
]

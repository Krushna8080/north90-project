from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message
from django.db import models 
@login_required
def chat_view(request, user_id=None):
    users = User.objects.exclude(id=request.user.id)
    selected_user = None
    messages = []
    
    if user_id:
        selected_user = User.objects.get(id=user_id)
        messages = Message.objects.filter(
    (models.Q(sender=request.user, receiver=selected_user) |
     models.Q(sender=selected_user, receiver=request.user))
    ).distinct().order_by('timestamp')

    
    return render(request, 'chat/chat.html', {
        'users': users,
        'selected_user': selected_user,
        'messages': messages
    })

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})
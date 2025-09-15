from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import CustomUser
from .models import Message

@login_required
def chat_view(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        text = request.POST.get("message")
        if text:
            Message.objects.create(
                sender=request.user,
                receiver=target_user,
                text=text
            )
            return redirect('chat_view', user_id=target_user.id)

    # Get chat history between the two users
    messages = Message.objects.filter(
        sender__in=[request.user, target_user],
        receiver__in=[request.user, target_user]
    ).order_by('timestamp')

    return render(request, 'chat/chat_view.html', {
        'target_user': target_user,
        'messages': messages
    })

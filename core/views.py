from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import CustomUser


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def user_list(request):
    users = CustomUser.objects.exclude(id=request.user.id)
    return render(request, 'core/user_list.html', {'users': users})

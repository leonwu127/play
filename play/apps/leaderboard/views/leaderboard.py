from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'leaderboard/index.html', {
        'user': request.user,
    })

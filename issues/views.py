from django.shortcuts import render, redirect
from .models import Issue

def issue_board(request):
    columns = [
        ('Backlog', Issue.objects.filter(status='backlog')),
        ('Ready', Issue.objects.filter(status='ready')),
        ('In Progress', Issue.objects.filter(status='in_progress')),
        ('In Review', Issue.objects.filter(status='in_review')),
        ('Done', Issue.objects.filter(status='done')),
    ]
    context = {
        'columns': columns,
    }
    return render(request, 'issues/issue_board.html', context)

def issue_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        status = request.POST.get('status', 'backlog')

        if title:
            Issue.objects.create(title=title, description=description, status=status)
            return redirect('issues:list')  # redirect to the board

    return redirect('issues:list')
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()

    title_filter = request.GET.get('title', '')  
    completed_filter = request.GET.get('completed', None) 

    filter_params = {}
    
    if title_filter:
        items = items.filter(title__icontains=title_filter)
        filter_params['title'] = title_filter  

    if completed_filter in ['true', 'false']:
        completed_filter = completed_filter.lower() == 'true'
        items = items.filter(completed=completed_filter)
        filter_params['completed'] = completed_filter  

    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            TodoItem.objects.create(title=title)
            return redirect('todo_list')

    return render(request, 'todo/todo_list.html', {
        'items': items,
        'title_filter': title_filter,
        'completed_filter': completed_filter,
        'filter_params': filter_params,
    })


def edit_todo(request, id):
    item = get_object_or_404(TodoItem, id=id)

    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            item.title = title
            item.save()
            return redirect('todo_list')

    return render(request, 'todo/edit_todo.html', {'item': item})

def complete_todo(request, id):
    item = TodoItem.objects.get(id=id)
    item.completed = True
    item.save()
    return redirect('todo_list')

def delete_todo(request, id):
    item = TodoItem.objects.get(id=id)
    item.delete()
    return redirect('todo_list')

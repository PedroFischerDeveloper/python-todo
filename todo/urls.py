from django.urls import path
from .views import todo_list, complete_todo, delete_todo, edit_todo

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('complete/<int:id>/', complete_todo, name='complete_todo'),
    path('delete/<int:id>/', delete_todo, name='delete_todo'),
    path('edit/<int:id>/', edit_todo, name='edit_todo'),  # Nova URL para edição
]

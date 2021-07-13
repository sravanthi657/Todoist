from django.urls import path
from . import views

urlpatterns =[
    path('list/',views.list_todo_item,name='list'),
    path('insert_todo/',views.insert_todo_item,name='insertTodo'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='deleteTodo'),
]
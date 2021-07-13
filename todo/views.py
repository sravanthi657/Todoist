import todo
from django.http.request import HttpRequest
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Todo
from django import forms
# Create your views here.
def list_todo_item(request):
    context= {'todo_list': Todo.objects.all()}
    return render(request,'todo/todo_list.html',context)
def insert_todo_item(request:HttpRequest):
    todo= Todo(details= request.POST['formContent'])
    todo.save()
    return redirect('/todo/list')
def delete_todo_item(request,todo_id):
    todo_to_delete=Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo_to_delete.delete()
        return redirect('/todo/list')
    context={'todoz':todo_to_delete}
    return render(request,'todo/del_warn.html',context)
   
    # return redirect('/todo/list')
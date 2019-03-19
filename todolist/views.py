from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import TodoList, Status
def index(request): 
    todos = TodoList.objects.all() 
    status_all = Status.objects.all() 
    if request.method == "POST": 
        if "taskAdd" in request.POST: 
            title = request.POST["title"] 
            content = request.POST["content"] 
            date = str(request.POST["date"]) 
            status = request.POST["status_select"] 
            contents = title + " -- " + date + " " + status 
            Todo = TodoList(title=title, content=contents, due_date=date, status=Status.objects.get(name=status))
            Todo.save() 
            return redirect("/") 
        if "taskDelete" in request.POST: 
            checkedlist = request.POST["checkedbox"] 
            # for todo_id in checkedlist:    
            todo = TodoList.objects.get(status = '2') 
            todo.delete() 
    return render(request, "index.html", {"todos": todos, "status_all":status_all})

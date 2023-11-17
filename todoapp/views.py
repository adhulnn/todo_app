from django.shortcuts import render,redirect
from .models import Task   
from .forms import TaskForm

# Create your views here.
def tasks(req):
    tasks=Task.objects.filter(completed=False)
    ctasks=Task.objects.filter(completed=True)
    if req.method == 'POST':
        name=req.POST.get('task')
        notes=req.POST.get('notes')
        due_date=req.POST.get('due_date')
        priority=req.POST.get('priority')
        task=Task(title=name, priority=priority,notes=notes,due_date=due_date)
        task.save()
        print(name, priority,'saved successfully')
    return render(req, 'todo.html', {'tasks':tasks,'ctasks':ctasks})

def edit_task(req,id):
    task=Task.objects.get(id=id)
    if req.method=='POST':
        form=TaskForm(req.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=TaskForm(instance=task)
    return render(req,'edit.html',{'form':form})

def delete_task(req,id):
    task=Task.objects.get(id=id)
    task.delete()
    print('deleted successfully')
    return redirect('/')

def mark_as_completed(req,id):
    task=Task.objects.get(id=id)
    task.completed=True
    task.save()
    return redirect('/')


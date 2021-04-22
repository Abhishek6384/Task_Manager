from django.shortcuts import render,redirect

from django.http import HttpResponse


from .models import tasks
from .forms import *
def index(request):
    
    t=tasks.objects.all()
    form=TaskFrom()

    context={'tasks':t,'form':form}
    if request.method =='POST':

        form=TaskFrom(request.POST)
        if form.is_valid():
             form.save()
        return redirect('/')
       
    return render(request,'list.html',context)    


def updateTask(request,pk):
    task= tasks.objects.get(id=pk)

    
    form=TaskFrom(instance=task)
    if request.method =='POST':
        form=TaskFrom(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'updata_task.html',context)


def deleteTask(request,pk):
    item=tasks.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'delete.html',context)
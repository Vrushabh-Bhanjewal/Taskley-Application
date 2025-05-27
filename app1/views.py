from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib .auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

@login_required
def todoList(request):
    data=Task.objects.filter(user=request.user)
    return render(request,'app1/todo_list.html',{'data':data})

@login_required
def todoDetails(request,myid):
    data=Task.objects.get(id=myid)
    print(data)
    return render(request,'app1/todo_details.html',{'task':data})

@login_required
def todoDelete(request,id):
    task=get_object_or_404(Task,id=id,user=request.user)
    task.delete()
    return redirect('list')

@login_required
def todoCreate(request):
    if (request.method=='POST'):
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        complete=request.POST.get('complete')=='on'
        t1=Task(user=request.user,title=title,desc=desc,complete=complete)
        t1.save()
        print("print: ",t1)
        print(title,desc,complete)
        return redirect('list')
    else:
        print('print: get method')
        return render(request,'app1/todo_create.html')


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('list')
    else:
        initial_data={'username':'','password':''}
        form=AuthenticationForm(initial=initial_data)
    return render(request,'user/login.html',{'form':form})

def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('list')
    else:
        initial_data={'username':'','password1':'','password2':''}
        form=UserCreationForm(initial=initial_data)
    return render(request,'user/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

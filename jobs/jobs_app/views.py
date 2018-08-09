from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import addJobForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    

    
    return render(request, 'index.html')

    

def alljobs(request):
    

    
    return render(request, 'alljobs.html')


def addjob(request):
    current_user = request.user
    if request.method == 'POST':
        form = addJobForm(request.POST)
        if form.is_valid():
            addjob=form.save(commit=False)
            addjob.user = current_user
            addjob.save()
            return HttpResponseRedirect('/')

    else:
        form = addJobForm()
   
    
    
    return render(request, 'addjob.html',{"form":form})


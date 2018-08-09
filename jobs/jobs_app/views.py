from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    

    
    return render(request, 'index.html')

    

def alljobs(request):
    

    
    return render(request, 'alljobs.html')


def addjob(request):
    

    
    return render(request, 'addjob.html')



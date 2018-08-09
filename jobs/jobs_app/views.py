from django.shortcuts import render

# Create your views here.
def index(request):
    

    
    return render(request, 'index.html')

def alljobs(request):
    

    
    return render(request, 'alljobs.html')
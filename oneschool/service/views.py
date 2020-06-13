from django.shortcuts import render

# Create your views here.

def cours(request):
    
    data = {
        
    }
    
    return render(request, 'course-single.html', data)

def programme(request):
    
    data = {
        
    }
    
    return render(request, 'index.html', data) 

def teacher(request):
    
    data = {
        
    }
    
    return render(request, 'course-single.html', data)       
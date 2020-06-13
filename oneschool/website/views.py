from django.shortcuts import render

# Create your views here.

def index(request):
    
    data = {
        
    }
    
    return render(request, 'index.html', data)


def course_single(request):
    
    data = {
        
    }
    
    return render(request, 'course-single.html', data)

def contact(request):
    
    data = {
        
    }
    
    return render(request, 'index.html', data)    
"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from .models import Post
from django.http import HttpRequest


def createpost(request):
        if request.method == 'POST':
            if request.POST.get('sapname') and request.POST.get('vorname'):
                post=Post()
                post.title= request.POST.get('sapname')
                post.content= request.POST.get('vorname')
                post.save()
                
                return render(request, 'app/index.html')  

        else:
                return render(request,'app/index.html')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

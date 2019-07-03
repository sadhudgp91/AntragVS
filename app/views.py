"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from .models import Post
from django.http import HttpRequest
from .forms import ContractForm, DownloadForm


"Kaushik: Create functions for CSV/PDF download"

def get_csv_data(starting_date, ending_date):
    """
    Prepare data in csv format for download, download_data
    """
    data = []
    num = 10
    for n in xrange(num):
        person = 'Person {}'.format(n + 1)
        type_contract = 'Some contract'
        start_date = starting_date
        end_date = ending_date
        data.append(', '.join([start_date, end_date, person, type_contract]))
    return '\n'.join(data)

def download_data(request):
    """
    Process a request to download data.
    * POST must contain 'starting_date' and 'ending_date'.
    """
    from django.http import HttpResponse

    try:
        assert request.method == 'POST'
        form = DownloadForm(request.POST)
        assert form.is_valid()
        starting_date = form.cleaned_data.get('starting_date')
        ending_date = form.cleaned_data.get('ending_date')
        assert starting_date and ending_date
        contracts = get_csv_data(starting_date, ending_date)
        assert contracts
    except AssertionError:
        error = 'Your request has some problems.'
        contracts = error

    attachment = 'contract_data.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(attachment)
    response.write(contracts)
    return response


"Kaushik: End of Function"



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

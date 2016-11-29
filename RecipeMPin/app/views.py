"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import Loginpin, Register


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        })


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'You can contact us at:',
            'year': datetime.now().year,
        })


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'M-Pin project for the Computer Systems Security class of the Master in Software Engineering at the Mathematics Research Center A.C.',
            'year': datetime.now().year,
        })


def loginpin(request):
    """Renders the contact page."""
    form_class = Loginpin
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('password'
            , '')
            with open('pin.txt', 'w+') as file:
                file.write(contact_name)

    assert isinstance(request, HttpRequest)
    return render(request,
        'app/loginpin.html',
        {
            'form': form_class,
            'title': 'About',
        })

def register(request):
    """Renders the contact page."""
    form_class = Register
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('password'
            , '')
            with open('registro.txt', 'w+') as file:
                file.write(contact_name)

    assert isinstance(request, HttpRequest)
    return render(request,
        'app/register.html',
        {
            'form': form_class,
            'title': 'About',
        })
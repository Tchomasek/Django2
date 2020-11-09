from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    context = {
        "title": "this is contact",
        'text': 'this is text',
        'number': 1,
        'list': [10,20,30,40,50,60,70],
        "my_html": "<h1>Hello world</h1>"

        }
    return render(request, 'contact.html', context)

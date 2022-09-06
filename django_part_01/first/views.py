from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Ola Mundo!")


def help(request):
    response_dict = {
        "help_response": "HELP PAGE"
    }
    return render(request, 'help/help.html', context=response_dict)
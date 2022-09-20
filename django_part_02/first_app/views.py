from django.shortcuts import render

# Create your views here.
def index(request):
    responde_dict = {"response": "Hello from first app"}
    return render(request, 'first_app/index.html', context=responde_dict)
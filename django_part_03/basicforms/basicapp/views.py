from django.shortcuts import render
from basicforms import forms

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print(f"NAME: {form.cleaned_data['name']}")

    return render(request,'basicapp/form_page.html',{'form':form})

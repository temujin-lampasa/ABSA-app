from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoLinkForm

# Create your views here.

def index(request):

    context = {}
    if request.method=="POST":
        form = VideoLinkForm(request.POST)
        if form.is_valid():
            context['response'] = "Form is valid"
        else:
            context['response'] = "Form is NOT valid"
    else:
        form = VideoLinkForm()
    
    context['form'] = form
    return render(request, "absa_app/index.html", context)
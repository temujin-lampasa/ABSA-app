from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoLinkForm

# Create your views here.

def index(request):
    print("METHOD", request.method)

    context = {}
    if request.method=="POST":
        print("POST req made")
        form = VideoLinkForm(request.POST)
        if form.is_valid():
            print("VALID POST")
            print("CLEANED:", form.cleaned_data)
            context['video_link'] = form.cleaned_data.get('video_link')
            context['response'] = f"Form is valid. Downloading {context.get('video_link')}..."
        else:
            print("FAILED")
            context['response'] = "Form is NOT valid"
    else:
        form = VideoLinkForm()
    
    context['form'] = form
    context['test'] = 'hello'
    return render(request, "absa_app/index.html", context)
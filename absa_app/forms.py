from django import forms

class VideoLinkForm(forms.Form):
    viideo_link = forms.CharField(label="Link:", max_length=100)
    
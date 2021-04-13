from django import forms

class VideoLinkForm(forms.Form):
    video_link = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Link'}))

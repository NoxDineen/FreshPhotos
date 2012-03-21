from django import forms
from photos.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo

class CommentForm(forms.Form):
	name = forms.CharField(max_length=255)
	email = forms.EmailField(max_length=255)
	comment = forms.CharField(max_length=2500, widget=forms.Textarea)
	
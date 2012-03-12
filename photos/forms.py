from django import forms

class CommentForm(forms.Form):
	name = forms.CharField(max_length=255)
	email = forms.EmailField(max_length=255)
	comment = forms.CharField(max_length=2500, widget=forms.Textarea)
	
from django.http import HttpResponse, HttpResponseRedirect
from photos.models import Gallery
from photos.models import Photo
from photos.models import Comment
from django.http import Http404
from django.shortcuts import render
from photos.forms import CommentForm

def gallery(request, gallery_key, view='grid'):
    try:
    	if gallery_key.isdigit():
        	mygallery = Gallery.objects.get(id=gallery_key)
        else:
        	mygallery = Gallery.objects.get(name=gallery_key)
    except Gallery.DoesNotExist:
        raise Http404
    context = {'gallery' : mygallery}
    return render(request, "my-gallery.html", context)
        

def photo(request, photo_id):
	try:
		myphoto = Photo.objects.get(id=photo_id)
	except Photo.DoesNotExist:
		raise Http404
	if request.method =='POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = Comment()
			new_comment.comment = form.cleaned_data['comment']
			new_comment.name = form.cleaned_data['name']
			new_comment.email = form.cleaned_data['email']
			new_comment.photo_id = myphoto.id
			new_comment.save()
			return HttpResponseRedirect('/photo/%d' % myphoto.id)
	else:
		form = CommentForm()
	comments = Comment.objects.filter(photo=photo_id)
	return render(request, 'photo-detail.html', {'photo' : myphoto, 'form' : form, 'comments' : comments})
    
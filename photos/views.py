from django.http import HttpResponse
from photos.models import Gallery
from photos.models import Photo
from django.http import Http404
from django.shortcuts import render

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
        
    
def photo(request, photo_key):
	try:
		if photo_key.isdigit():
			myphoto = Photo.objects.get(id=photo_key)
		else:
			myphoto = Photo.objects.get(name=photo_key)
	except Photo.DoesNotExist:
		raise Http404
	context = {'photo': myphoto}
	return render(request, "photo-detail.html", context)
    

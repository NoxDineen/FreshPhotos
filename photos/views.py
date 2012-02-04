from django.http import HttpResponse
from photos.models import Gallery
from photos.models import Photo
from django.http import Http404
from django.shortcuts import render

def gallery(request, gallery_key):
    try:
    	if gallery_key.isdigit():
        	mygallery = Gallery.objects.get(id=gallery_key)
        else:
        	mygallery = Gallery.objects.get(name=gallery_key)
    except Gallery.DoesNotExist:
        raise Http404
    return HttpResponse(mygallery.name + "<br />" + mygallery.description)
        
    
def photo(request, photo_id):
    myphoto = Photo.objects.get(id=photo_id)
    context = {'photo': myphoto}
    return render(request, "photo.html", context)
    

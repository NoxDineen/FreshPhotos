# Create your views here.
from django.http import HttpResponse
from photos.models import Gallery
from photos.models import Photo
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render

# def gallery(request, gallery_id):
# 	mygallery = get_object_or_404(Gallery, pk=gallery_id)
# 	return HttpResponse(mygallery.name + '<br />' + mygallery.description)

def gallery(request, url_key):
	#try:
		#if url_key.isdigit():
		mygallery = get_object_or_404(Gallery, pk=int(url_key))
		#	mygallery = Gallery.objects.get(id=url_key)
		#else:
		mygallery = Gallery.objects.all().filter(name=url_key).get()
		#	my gallery = Gallery.objects.get(name='url_key')
		return HttpResponse(mygallery.name + '<br />' + mygallery.description)
	#except Gallery.DoesNotExist:
		#raise Http404



def photo(request, url_key):
	if url_key.isdigit():
		myphoto = get_object_or_404(Photo, pk=int(url_key))
	else:
		myphoto = Photo.objects.all().filter(name=url_key).get()
	#return HttpResponse(myphoto.name + '<br />' + '<img src="' + myphoto.filename.url + '" />')
	context = {'photo' : myphoto}
	return render(request, "photo.html", context)
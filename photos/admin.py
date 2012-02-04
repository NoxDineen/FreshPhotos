from django.contrib import admin
from photos.models import Gallery
from photos.models import Photo

class GalleryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')
	list_display_links = ('name',)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('id', 'picture', 'name', 'created', 'filename', 'visible_by')
	list_display_links = ('picture', 'name',)
	list_filter = ('visible_by',)
	filter_horizontal = ('galleries',)

	def picture(self, photo):
		return '<img src="%s" height="150"/>' % photo.filename.url
	picture.allow_tags = True

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
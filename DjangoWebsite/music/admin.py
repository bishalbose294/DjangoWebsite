from django.contrib import admin
from .models import Album, Song

#username : admin
#password : admin1234

admin.site.register(Album)
admin.site.register(Song)
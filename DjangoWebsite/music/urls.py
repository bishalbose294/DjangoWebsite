from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns=[

    # /music/
    url(r"^$", views.IndexView.as_view(), name="index"),

    url(r"^register/$",views.UserFormView.as_view(), name="register"),

    # /music/<album_id>/
    url(r"^(?P<pk>[0-9]+)/$", views.DetailView.as_view(), name="detail"),

    # /music/album/add/
    url(r"album/add/$", views.AlbumCreate.as_view(), name="album-add"),

    # /music/<album_id>/favourite/
    url(r"^(?P<album_id>[0-9]+)/favourite/$", views.favourite, name="favourite"),

    # /music/<album_id>/update/
    url(r"^(?P<pk>[0-9]+)/update/$", views.AlbumUpdate.as_view(), name="album-update"),

    # /music/<album_id>/delete/
    url(r"^(?P<pk>[0-9]+)/delete/$", views.AlbumDelete.as_view(), name="album-delete"),
]


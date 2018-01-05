from django.conf.urls import url

from notebook import views


urlpatterns = [
    url(r'^$', views.notes, name='notes'),
    url(r'^create$', views.create, name='create'),
    url(r'^update$', views.update, name='update'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
]

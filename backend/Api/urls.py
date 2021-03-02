from django.conf.urls import url
from Api import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url (r'^User/$', views.objectCaller),
    url(r'^User/([0-9]+)$', views.objectCaller)
]
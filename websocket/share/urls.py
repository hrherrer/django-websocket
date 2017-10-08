from django.conf.urls import url
from .views import *

from . import views

urlpatterns = [
    url(r'^qr/(?P<pk>\d+)$', QRDetailView.as_view(), name="qr_code"),
    url(r'^profile/(?P<pk>\d+)$', UserProfileView.as_view(), name="profile"),
]
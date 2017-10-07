from django.conf.urls import url
from .views import *

from . import views

urlpatterns = [
    url(r'^register/$', UserCreateView.as_view(), name="register"),
    url(r'^login/$', UserLoginView.as_view(), name="login"),
    url(r'^logout/$', UserLogoutView.as_view(), name="logout"),
    url(r'^profile/(?P<pk>\d+)/$', UserProfileView.as_view(), name="profile"),
]
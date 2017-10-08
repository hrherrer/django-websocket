from django.contrib.auth.models import User
from django.views import generic
from account.models import QRCode, Scan
from .services import get_client_ip
from django.shortcuts import render

# Create your views here.

class QRDetailView(generic.DetailView):
    model = QRCode
    template_name = 'share/qrcode_detail.html'

class UserProfileView(generic.DetailView):
    model = User
    template_name = 'share/profile_detail.html'

    def get(self, request, *args, **kwargs):
        # Do Something
        print(get_client_ip(request))
        print(request.META['HTTP_USER_AGENT'])
        return super().get(request, *args, **kwargs)
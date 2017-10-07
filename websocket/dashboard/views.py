from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import generic


# Create your views here.

class IndexView(UserPassesTestMixin, generic.View):
    login_url = '/account/login/'
    def get(self, request):
        return render(request, 'dashboard/index.html')

    def test_func(self):
        return self.request.user.is_authenticated

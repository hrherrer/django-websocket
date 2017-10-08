from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from account.forms import RegisterForm, LoginForm, ProfileForm


# Create your views here.

class UserCreateView(generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'account/user_form.html'
    success_url = reverse_lazy('dashboard:register_user')




class UserLoginView(UserPassesTestMixin, generic.View):
    login_url = '/'
    redirect_field_name = ''
    def get(self, request):
        return render(request, 'account/login_form.html', context={
            'form': LoginForm,
        })

    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return render(request, 'account/login_form.html', context={
                'err_message': 'Credenciales invalidas.',
                'form': LoginForm
            })

    def test_func(self):
        return not self.request.user.is_authenticated


class UserLogoutView(generic.View):
    def get(self, request):
        if self.request.user.is_authenticated:
            logout(request)
        return redirect('account:login')

class UserProfileView(generic.UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'account/profile_form.html'
    success_url = '/'

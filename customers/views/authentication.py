from django.shortcuts import render, redirect

from customers.forms import CustomerLoginForm
from django.http import HttpResponse
# Create your views here.
from django.views import View


from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


from django.contrib.auth import logout


class Login(View):
    context = {
        'errors': '',
        'form': CustomerLoginForm()
    }

    def get(self, request):

        return render(request, 'login.html', self.context)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            self.context['errors'] = 'Invalid email or password'
            # print(self.context)
            return render(request, 'login.html', self.context)


def logout_view(request):
    logout(request)
    return redirect('login')

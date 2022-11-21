from django.shortcuts import render, redirect

from customers.forms import CustomerLoginForm
from django.http import HttpResponse
# Create your views here.
from django.views import View


from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


from django.contrib import messages

from django.utils.decorators import method_decorator
from customers.decorators import persist_session_vars


@method_decorator(persist_session_vars(['carts']), name='dispatch')

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
            messages.success(request, "You have logged in successfully.")
            return redirect('index')

        else:
            messages.error(request, "Invalid email or password.")

            # print(self.context)
            return redirect('login')

@method_decorator(persist_session_vars(['cart']), name='dispatch')
class Logout(View):
    def get(self,request):
        logout(request)
        messages.success(request, "You have logged out successfully.")

        return redirect('login')

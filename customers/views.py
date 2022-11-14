from django.shortcuts import render, redirect
from .forms import CustomerForm
from .forms import CustomerLoginForm
from django.http import HttpResponse
# Create your views here.
from django.views import View
from .models.customer import Customer

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('login')
    # Redirect to a success page.


class Signup(View):
    def get(self, request):
        context = {
            'form': CustomerForm()
        }
        return render(request, 'signup.html', context)

    def post(self, request):
        post_data = request.POST
        username = post_data.get('username')
        email = post_data.get('email')
        full_name = post_data.get('full_name')
        phone_number = post_data.get('phone_number')
        password = post_data.get('password')
        customer = Customer.objects.create_user(username=username, email=email, full_name=full_name,
                                                phone_number=phone_number, password=password)
        customer.register()

        return redirect('login')


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

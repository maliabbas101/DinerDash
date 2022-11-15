from django.shortcuts import render, redirect
from customers.forms import CustomerForm
from django.http import HttpResponse
# Create your views here.
from django.views import View
from customers.models.customer import Customer


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

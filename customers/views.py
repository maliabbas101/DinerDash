from django.shortcuts import render
from .forms import CustomerForm
from django.http import HttpResponse
# Create your views here.
from django.views import View


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
        phone_number = post_data.get('phone_number')
        password = post_data.get('password')

        return HttpResponse(request.POST.get('email'))


# def signup(request):
#     pass

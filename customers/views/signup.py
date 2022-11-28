from django.shortcuts import render, redirect
from customers.forms import CustomerForm
from django.http import HttpResponse
# Create your views here.
from django.views import View
from customers.models.customer import Customer
from django.contrib import messages


class Signup(View):
    form = CustomerForm()

    def check_user(self, form_email):
        user_length = Customer.objects.filter(email=form_email).count()
        if user_length > 0:
            self.form.errors.update(({'Email Integrity Error': "Email already exists."})
                                    )
            return False
        return True

    def check_password(self, password, confirm_password):
        if len(password) < 6:
            self.form.errors.update(({'Password Length': "Password is too short."})
                                    )
            return False
        else:
            if password != confirm_password:
                self.form.errors.update(({'Password Confirmation': "Passwords don't match."})
                                        )
                return False
            return True

    def get(self, request):
        context = {
            'form': self.form
        }
        return render(request, 'signup.html', context)

    def post(self, request):

        post_data = request.POST
        username = post_data.get('username')
        email = post_data.get('email')
        full_name = post_data.get('full_name')
        phone_number = post_data.get('phone_number')
        password = post_data.get('password')
        confirm_password = post_data.get('confirm_password')
        group = post_data.get('groups')

        email_check = self.check_user(email)
        password_check = self.check_password(password, confirm_password)

        if email_check and password_check:
            customer = Customer.objects.create_user(username=username, email=email, full_name=full_name,
                                                    phone_number=phone_number, password=password)
            customer.register()
            customer.groups.set(group)
            customer.register()
            messages.success(request, "Registration successfull.")

            return redirect('login')
        else:
            for error in self.form.errors.values():

                messages.error(request, error)
            self.form.errors.clear()
            return redirect('signup')

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth import authenticate, login
# Create your views here.
@csrf_protect
def user_account(request):
    # errors_login = ['give valid email in login', 'fill all the fields in login']
    # errors_register = ['give valid email', 'fill all the fields']
    # cotext = {
    #     'login_message' : errors_login,
    #     'register_message' : errors_register
    # }
    context = {}
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        if form_id == 'register':
            context['register'] = True
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')
                address = request.POST.get('address')
                number = request.POST.get('number')
                cpassword = request.POST.get('cpassword')
                user = User.objects.create_user(  # Inbuilt user want to create the method using create_user
                    username = username,
                    password = password,
                    email = email,
                )
                Customer.objects.create(
                    user = user,
                    phone_number = number,
                    address = address
                )
                success_message = 'Registration successful'
                messages.success(request, success_message)
            except Exception as e:
                error_message = 'Duplicate user name or invalid credentials'
                print('error----->',e)
                messages.error(request, error_message)


        elif form_id == 'login':
            context['register'] = False
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password) #checking the given username and password is existing or not
            print('HEate---->',username, password)
            if user:
                login(request, user) # if the user is exists it gives the user to login
                return redirect('index')
            else:
                error_message = 'Invalid user credentials'
                messages.error(request, error_message)

        else:
            messages.error(request, 'Invalid form submission')
            return redirect('user_account')

    return render(request, 'account.html', context)
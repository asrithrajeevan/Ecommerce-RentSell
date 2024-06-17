from django.shortcuts import render

# Create your views here.
def user_account(request):
    errors_login = ['give valid email in login', 'fill all the fields in login']
    errors_register = ['give valid email', 'fill all the fields']
    cotext = {
        'login_message' : errors_login,
        'register_message' : errors_register
    }
    return render(request, 'account.html', cotext)
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login

def user_login(request):
    '''
    Login
    '''
    if request.method == 'POST':
            user = authenticate(
                username=request.POST['email'],
                password=request.POST['password']
            )
            if user is not None:
                login(request, user)
                return redirect(dashboard)
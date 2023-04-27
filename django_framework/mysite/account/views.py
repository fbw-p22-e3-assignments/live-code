from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.models import User


# def user_login(request):
#     """
#     This is for logging in.
#     """
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, 
#                                 username=cd['username'], 
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated Successfully!')
#                 else:
#                     return HttpResponse('Your account is disabled!')
#             else:
#                 return HttpResponse('Invalid credentials!')
#     else:
#         form = LoginForm()
        
#     return render(request, 'account/login.html', {"form": form})   


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            print(new_user)
            new_user.save()
            # User.objects.create(user=new_user)
            return redirect('account:login')
    else:
        user_form = UserRegistrationForm()
        
    return render(request, 'account/register.html', {"user_form": user_form})
        

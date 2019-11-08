from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import NameForm
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .forms import ContactForm

from django.urls import reverse_lazy
from django.views import generic



def navbar(request):
    isauthen = request.user.is_authenticated
    return render(request ,'index.html' , {'isauth' : isauthen})

def sign_up(request):

    if request.method=='POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/app')
    else:
        form = NameForm()

    return render(request , 'sign_up.html',{'form' : form})

def log_in(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is None:
            messages.error(request, 'username or password not correct')
            return render(request, 'login.html', {"error": True})
        else:
            login(request,user)
            return HttpResponseRedirect('/')

    return render(request,'login.html')


def log_out(request):
    logout(request)
    return  HttpResponseRedirect('/login')


def signup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/app')
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            first_name =form.cleaned_data.get('firstname')
            last_name=form.cleaned_data.get('lastname')

            user = authenticate(username=username, password=password ,
                                email=email,firstname=first_name,lastname=last_name)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




def contact(request):
    if request.method=='POST':
        form_class = ContactForm(request.POST)
        if form_class.is_valid():
            return redirect('index')

    form_class = ContactForm
    return render(request, 'contact.html', {'form': form_class, })

#@login_required
#def user_profile(request):
#    return render(request , 'user-profile.html')





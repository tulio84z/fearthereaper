from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from . import forms


@login_required
def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user_name, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form})

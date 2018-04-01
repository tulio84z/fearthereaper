from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from .forms import SignUpForm
from .lifeexpectancy import get_life_expectancy

@login_required
def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            birthday = form.cleaned_data['birthday']
            gender = form.cleaned_data['gender']
            nationality = form.cleaned_data['nationality']

            life_span = get_life_expectancy(gender, nationality, birthday)
            life_span = int(life_span)

            form.save()
            user_name = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user_name, password=raw_password)
            login(request, user)
            user.life_expectancy = life_span
            user.save()
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

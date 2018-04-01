from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db import transaction

from .forms import SignUpForm
from .lifeexpectancy import get_life_expectancy, calculate_current_week_num
from core.models import Week


@login_required
def index(request):
    current_user = request.user

    weeks = Week.objects.all()
    context = {'weeks': weeks}

    return render(request, 'index.html', context)

@login_required
def show_week(request, week_num):
    current_user = request.user

    week = Week.objects.get(week_num=week_num, user_id=current_user.id)
    context = {'week': week}

    return render(request, 'week.html', context)


@transaction.atomic
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
            _initialize_life_span_info(user, life_span)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def _initialize_life_span_info(user, life_span):
    user.life_expectancy = life_span

    life_span_in_weeks = life_span * 52
    user.life_in_weeks = life_span_in_weeks

    user.save()

    current_week_num = calculate_current_week_num(user.birthday)

    for week_num in range(1, life_span_in_weeks + 1):
        week = Week()
        week.user = user
        week.week_num = week_num

        if week_num < current_week_num:
            week.week_status = Week.PAST_WEEK_BEFORE_SIGNUP
        elif week_num == current_week_num:
            week.week_status = Week.CURRENT_WEEK_NO_OBJ
        elif week_num == life_span_in_weeks:
            week.week_status = Week.DEATH
        else:
            week.week_status = Week.FUTURE_WEEK_NO_OBJ

        week.save()

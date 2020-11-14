from django.core.paginator import Paginator
from django.db.models import Count, Sum
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

from donation.models import (
    Category,
    Donation,
    Insitution,
)

from donation.forms import (
    CreateUserForm,
    LoginForm
)


class LandingPage(View):
    def get(self, request):
        total_quantity = Donation.objects.all().aggregate(Sum('quantity'))
        total_institutions = Donation.objects.all().aggregate(Count('institution', distinct=True))
        foundations = Insitution.objects.filter(type=1)
        non_governmental_institutions = Insitution.objects.filter(type=2)
        local_collections = Insitution.objects.filter(type=3)
        paginator_foundations = Paginator(foundations, 3)
        page = request.GET.get('page')
        foundations_paginated = paginator_foundations.get_page(page)
        ctx = {
            'total_quantity': total_quantity,
            'total_institutions': total_institutions,
            'foundations': foundations_paginated,
            'non_governmental_insitutions': non_governmental_institutions,
            'local_collections': local_collections,
        }
        return render(request, 'index.html', ctx)


class AddDonation(View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Insitution.objects.all()
        ctx = {
            'categories': categories,
            'institutions': institutions,
        }
        return render(request, 'form.html', ctx)


class Login(View):
    def get(self, request):
        form = LoginForm()
        ctx = {
            'form': form
        }
        return render(request, 'login.html', ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                msg = 'Podany użytkownik nie istnieje'
                form = CreateUserForm()
                ctx = {
                    'msg': msg,
                    'form': form
                }
                return render(request, 'register.html', ctx)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing-page')
            else:
                msg = 'Niepoprawne hasło'
                form = LoginForm()
                ctx = {
                    'msg': msg,
                    'form': form
                }
                return render(request, 'login.html', ctx)
        return render(request, 'login.html', {'form': form})


def logout_request(request):
    logout(request)
    return redirect('landing-page')


class Register(View):
    def get(self, request):
        form = CreateUserForm()
        ctx = {
            'form': form,
        }
        return render(request, 'register.html', ctx)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            new_user = User.objects.create(username=username,
                                           first_name=first_name,
                                           last_name=last_name,
                                           email=email)
            new_user.set_password(password)
            new_user.save()

            return redirect('login')
        return render(request, 'register.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            donations = user.donations.filter(is_taken=False)
            donations_taken = user.donations.filter(is_taken=True)
            ctx = {
                'user': user,
                'donations': donations,
                'donations_taken': donations_taken,
            }
            return render(request, 'profile.html', ctx)


class ChangeStatusDonation(View):
    def post(self, request, donation_id):
        donation = Donation.objects.get(pk=donation_id)
        donation.is_taken = True
        donation.save()
        user = request.user
        donations = user.donations.filter(is_taken=False)
        donations_taken = user.donations.filter(is_taken=True)
        ctx = {
            'user': user,
            'donations': donations,
            'donations_taken': donations_taken,
        }
        return render(request, 'profile.html', ctx)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from adminlawyer.models import *


def hello(request):
    return HttpResponse("Hello, World!")

def layout(request):
    context = {}
    return render(request,'client/layout.html',context)

def contact(request):
    result = Cases.objects.all()
    context = {'result':result}
    return render(request,'client/contact.html',context)


def cases(request):
    context = {}
    return render(request,'client/cases.html',context)


def appointment(request):
    context = {}
    return render(request,'client/appointment.html',context)


def header(request):
    context = {}
    return render(request,'client/header.html',context)

def sidebar(request):
    context = {}
    return render(request,'client/sidebar.html',context)

def footer(request):
    context = {}
    return render(request,'client/footer.html',context)

def home(request):
    context = {}
    return render(request,'client/home.html',context)

def menu(request):
    context = {}
    return render(request,'client/menu.html',context)


def login(request):
    context = {}
    return render(request,'client/login.html',context)


def login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(request, username=username, password=password)

    if result is None:
        print('Invalid Username Or Password')
        return redirect('/client/login')
    else:
        auth.login(request, result)
        return redirect('/client/home')


def logout(request):
    auth.logout(request)
    return redirect('/client/login')


def feedback_store(request):
    case  = request.POST['case']
    rating  = request.POST['rating']
    message = request.POST['message']
    id = request.user.id

    Feedback.objects.create(rating=rating,message=message, cases_id=case,user_id=id)
    messages.success(request, 'Thank you for your valuable feedback')

    return redirect('/client/contact')

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "users/profile.html"


def update_profile_about(request, slug):
    if request.method == "POST":
        user_form = UserForm(
            request.POST, instance=request.user, prefix="user")
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile, prefix="profile"
        )
        if all([user_form.is_valid(), profile_form.is_valid()]):
            us = user_form.save()
            prof = profile_form.save()

            prof.save()

            messages.success(request, _(
                "Your profile was successfully updated!"))
            return redirect("profile", slug=slug)
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        user_form = UserForm(instance=request.user, prefix="user")
        profile_form = ProfileForm(
            instance=request.user.profile, prefix="profile")
    return render(
        request,
        "users/profile_update_about.html",
        {"user_form": user_form, "profile_form": profile_form, },
    )

def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'users/partials/state_dropdown_list_options.html', {'states': states})


def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'users/partials/city_dropdown_list_options.html', {'cities': cities})


def load_streets(request):
    city_id = request.GET.get('city')
    streets = Street.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'users/partials/street_dropdown_list_options.html', {'streets': streets})
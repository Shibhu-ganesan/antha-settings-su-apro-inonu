from django.shortcuts import render, redirect
from .Forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import *
from django.core.mail import send_mail
from django.conf import settings


def dashboard(request):
    context = {}
    return render(request, "joinwithmeapp/dashboard.html", context)
'''
<!-- <li><a href="{% url 'reg_before' %}">Sign up</a></li>
            <li><a href="{% url 'login' %}">Login</a></li>
            <li><a href="{% url 'logout' %}">Logout</a></li> -->
'''
def member_page(request):
    context = {}
    return render(request, "joinwithmeapp/member.html", context)
def member_user(request):
    user = Member.objects.get(user = request.user)
    context = {'user': user}
    return render(request, 'joinwithmeapp/member_user.html', context)
def member_form(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        print(form.errors)
        if form.is_valid() == True:
            form.save()
            return redirect('mem_reg')
    context = {"form": form}

    return render(request, 'joinwithmeapp/member_form.html', context)

def member_register(request):
    group = None
    form = CreateUserForm()
    user = Member.objects.all()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            subject = 'Thank you......'
            message = 'Welcome da venna.'
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='member')
            user.groups.add(group)
            Member.objects.create(

                Name=user.username
            )
            messages.success(request, "Hell yeah Welcome" + username)
            return HttpResponseRedirect(reverse('login'))
    context = {"form": form}
    return render(request, 'joinwithmeapp/member_register.html', context)

def member_list(request):
    member = Member.objects.all()
    context = {'member': member}
    return render(request, 'joinwithmeapp/member_list.html', context)

def member_details(request,id):
    member = Member.objects.get(pk = id)
    context = {"user": member}
    return render(request, 'joinwithmeapp/details.html', context)

def member_settings(request,id):
    member = Member.objects.get(pk = id)
    form = MemberForm(instance=member)
    if request.method == 'POST':
        form = MemberForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member_user'))
    context = {"form": form}
    return render(request, 'joinwithmeapp/settings.html', context)


def startup_page(request):
    context = {}
    return render(request, "joinwithmeapp/startup.html", context)


def startup_user(request):
    user = StartUp.objects.get(user=request.user)
    context = {'user': user}
    return render(request, 'joinwithmeapp/startup_user.html', context)


def startup_form(request):
    form = StartUpForm()
    print(request.method)
    if request.method == "POST":
        form = StartUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sta_reg")

    context = {"form": form}
    return render(request, 'joinwithmeapp/startup_form.html', context)

def startup_register(request):
    group = None
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='startup_seeker')
            user.groups.add(group)
            StartUp.objects.create(
                user=user,
                Name=user.username
            )

            messages.success(request, "Hell yeah Welcome" + username)
            return redirect("login")
    context = {"form": form}
    return render(request, 'joinwithmeapp/startup_register.html', context)

def startup_list(request):
    startupseekers = Investor.objects.all()
    context = {'startupseekers': startupseekers}
    return render(request, 'joinwithmeapp/startup_list.html', context)


def startup_details(request,id):
    startup = StartUp.objects.get(pk = id)
    context = {"user": startup}
    return render(request, 'joinwithmeapp/details.html', context)

def startup_settings(request,id):
    startup = StartUp.objects.get(pk = id)
    form = StartUpForm(instance=startup)
    if request.method == 'POST':
        form = StartUpForm(request.POST,instance=startup)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('startup_user'))

    context = {"form": form}
    return render(request, 'joinwithmeapp/settings.html', context)
def investor_page(request):
    context = {}
    return render(request, "joinwithmeapp/investor.html", context)


def investor_user(request):
    user = Investor.objects.get(user=request.user)
    context = {'user': user}
    return render(request, 'joinwithmeapp/investor_user.html', context)
# <span><a href="{% url 'logout' %}"><button class="btn btn-sm btn-dark">Logout</button></a></span>
def investor_list(request):
    investor = Investor.objects.all()
    context = {'investor': investor}
    return render(request, 'joinwithmeapp/investor_list.html', context)






def investor_form(request):
    form = InvestorForm()
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inv_reg')
    context = {"form": form}

    return render(request, 'joinwithmeapp/investor_form.html', context)

def investor_register(request):
    group = None
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='investor')
            user.groups.add(group)
            Investor.objects.create(
                user=user,
                Name=user.username
            )

            messages.success(request, "Hell yeah Welcome" + username)
            return redirect("login")
    context = {"form": form}
    return render(request, 'joinwithmeapp/investor_register.html', context)


def investor_details(request,id):
    investor = Investor.objects.get(pk = id)
    context = {"user": investor}
    return render(request, 'joinwithmeapp/details.html', context)

def investor_settings(request,id):
    investor = Investor.objects.get(pk = id)
    form = InvestorForm(instance=investor)
    if request.method == 'POST':
        form = InvestorForm(request.POST,instance=investor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('investor_user'))

    context = {"form": form}
    return render(request, 'joinwithmeapp/settings.html', context)
def l_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            group = request.user.groups.all()[0].name
            if group == 'member':
                return HttpResponseRedirect(reverse('member_user'))
            if group == 'investor':
                return HttpResponseRedirect(reverse('investor_user'))
            if group == 'startup':
                return HttpResponseRedirect(reverse('startup_user'))
            group = None
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'joinwithmeapp/login.html', context)











def reg_before(request):
    context = {}
    return render(request, 'joinwithmeapp/reg_before_page.html', context)


def logoutt(req):
    logout(req)
    return l_login(req)





















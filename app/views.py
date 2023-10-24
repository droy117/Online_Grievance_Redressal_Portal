from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import User, Grievance, Escalate

def index(request):
    return render(request, 'app/index.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        address = request.POST["address"]
        state = request.POST["state"]
        gender = request.POST["gender"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password, email=email, phone_number=phone_number, address=address, state=state, gender=gender)
            user.save()
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "app/register.html")

def register_grievance(request): #dashboard
    registered = Grievance.objects.filter(status="REGISTERED", user=request.user)
    underReview = Grievance.objects.filter(status="UNDER REVIEW", user=request.user)
    closed = Grievance.objects.filter(status="CLOSED", user=request.user)
    nreg = len(registered)
    nureview = len(underReview)
    nclose = len(closed)
    grievances = Grievance.objects.filter(user=request.user)

    return render(request, 'app/registerGrievance.html', {
        "registerd": registered,
        "underReview": underReview,
        "closed": closed,
        "count_reg": nreg,
        "count_review": nureview,
        "count_closed": nclose,
        "grievances": grievances,
    })

def track_grievance(request):
    if request.method == "POST":
        try:
            grievance_obj = Grievance.objects.get(ref_no=request.POST["ref_no"], user=request.user)
            return render(request, "app/track.html", {
                "grievance": grievance_obj,
            })
        except Grievance.DoesNotExist:
            return render(request, "app/error.html", {
                "message": "Uh.. Oh! It seems the Reference Number is wrong. Please try again."
            })
    else:
        return render(request, 'app/track.html')

def lodge_grievance(request):
    if request.method == 'POST':
        category = request.POST["category"]
        about = request.POST["about"]
        details = request.POST["details"]

        grievance_obj = Grievance(user=request.user, category=category, details=details, about=about)
        grievance_obj.save()
        ref_no = 10000+grievance_obj.id
        grievance_obj.ref_no = ref_no
        grievance_obj.save()

        return render(request, 'app/success.html', {
            "ref_no": ref_no,
            "message": "Successfully Lodged Grievance."
        })
    else:
        return render(request, 'app/lodge.html')

def escalate(request):
    if request.method == 'POST':
        ref_no = request.POST["ref_no"]
        priority = request.POST["Priority"]
        reason = request.POST["reason"]

        print(f"REF: {ref_no}")

        try:
            grievance_obj = Grievance.objects.get(ref_no=ref_no)
            grievance_obj.priority = priority
            grievance_obj.save()
        except Grievance.DoesNotExist:
            return render(request, "app/error.html", {
                "message": "Uh.. Oh! It seems the Reference Number is wrong. Please try again."
            })

        escalate_obj = Escalate(ref_no=ref_no, reason=reason, priority=priority)
        escalate_obj.save()

        return render(request, 'app/success.html', {
            "ref_no": ref_no,
            "message": "Successfully Escalated Grievance."
        })
    else:
        return render(request, 'app/escalate.html')

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

logger = logging.getLogger(__name__)

def about(request):
    return render(request, 'djangoapp/about.html')

def contact(request):
    return render(request, 'djangoapp/contact.html')

def login_request(request):
    context = {}
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
        else:
            return JsonResponse({"userName": username, "status": "Failed"})
    return JsonResponse({"status": "GET not allowed"})

def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})

def registration(request):
    context = {}
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        try:
            User.objects.get(username=username)
            return JsonResponse({"userName": username, "error": "Already Registered"})
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email,
            )
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
    return JsonResponse({"status": "GET not allowed"})

def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

def get_dealer_details(request, dealer_id):
    context = {}
    return render(request, 'djangoapp/dealer_details.html', context)

def add_review(request, dealer_id):
    context = {}
    return render(request, 'djangoapp/add_review.html', context)
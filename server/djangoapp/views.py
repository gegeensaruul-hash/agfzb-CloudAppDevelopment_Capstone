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
    dealers = [
        {"id": 1, "name": "Best Cars Chicago", "city": "Chicago", "state": "IL", "address": "123 Main St", "zip": "60601"},
        {"id": 2, "name": "Top Autos New York", "city": "New York", "state": "NY", "address": "456 Broadway", "zip": "10001"},
        {"id": 3, "name": "Premier Motors LA", "city": "Los Angeles", "state": "CA", "address": "789 Sunset Blvd", "zip": "90001"},
        {"id": 4, "name": "Kansas City Motors", "city": "Kansas City", "state": "KS", "address": "321 Main St", "zip": "66101"},
        {"id": 5, "name": "Wichita Auto Group", "city": "Wichita", "state": "KS", "address": "654 Central Ave", "zip": "67202"},
    ]
    return render(request, 'djangoapp/index.html', {"dealers": dealers})

def get_dealer_details(request, dealer_id):
    reviews = [
        {"id": 1, "dealer_id": dealer_id, "review": "Great service!", "sentiment": "positive"},
        {"id": 2, "dealer_id": dealer_id, "review": "Good experience.", "sentiment": "positive"},
    ]
    return render(request, 'djangoapp/dealer_details.html', {"dealer_id": dealer_id, "reviews": reviews})

def get_dealers_by_state(request, state):
    all_dealers = [
        {"id": 1, "name": "Best Cars Chicago", "city": "Chicago", "state": "IL", "address": "123 Main St", "zip": "60601", "lat": "41.8781", "long": "-87.6298", "short_name": "Best Cars", "full_name": "Best Cars Chicago LLC"},
        {"id": 2, "name": "Top Autos New York", "city": "New York", "state": "NY", "address": "456 Broadway", "zip": "10001", "lat": "40.7128", "long": "-74.0060", "short_name": "Top Autos", "full_name": "Top Autos New York LLC"},
        {"id": 3, "name": "Premier Motors LA", "city": "Los Angeles", "state": "CA", "address": "789 Sunset Blvd", "zip": "90001", "lat": "34.0522", "long": "-118.2437", "short_name": "Premier Motors", "full_name": "Premier Motors LA LLC"},
        {"id": 4, "name": "Kansas City Motors", "city": "Kansas City", "state": "KS", "address": "321 Main St", "zip": "66101", "lat": "39.1141", "long": "-94.6275", "short_name": "KC Motors", "full_name": "Kansas City Motors LLC"},
        {"id": 5, "name": "Wichita Auto Group", "city": "Wichita", "state": "KS", "address": "654 Central Ave", "zip": "67202", "lat": "37.6872", "long": "-97.3301", "short_name": "Wichita Auto", "full_name": "Wichita Auto Group LLC"},
    ]
    filtered = [d for d in all_dealers if d["state"] == state.upper()]
    return JsonResponse({"dealers": filtered})

def get_car_makes(request):
    cars = [
        {"id": 1, "make": "Toyota", "model": "Camry"},
        {"id": 2, "make": "Honda", "model": "Civic"},
        {"id": 3, "make": "Ford", "model": "Mustang"},
    ]
    return JsonResponse({"CarModels": cars})

def analyze_review(request):
    review_text = request.GET.get('text', '')
    sentiment = "positive" if "fantastic" in review_text.lower() or "great" in review_text.lower() else "neutral"
    return JsonResponse({"sentiment": sentiment, "review": review_text})

def add_review(request, dealer_id):
    if request.method == "POST":
        review_text = request.POST.get('review', '')
        car_make = request.POST.get('car_make', '')
        car_model = request.POST.get('car_model', '')
        reviews = [
            {"id": 1, "dealer_id": dealer_id, "review": "Great service!", "sentiment": "positive"},
            {"id": 2, "dealer_id": dealer_id, "review": "Good experience.", "sentiment": "positive"},
            {"id": 3, "dealer_id": dealer_id, "review": review_text, "sentiment": "positive", "car": f"{car_make} {car_model}"},
        ]
        return render(request, 'djangoapp/dealer_details.html', {"dealer_id": dealer_id, "reviews": reviews})
    context = {"dealer_id": dealer_id}
    return render(request, 'djangoapp/add_review.html', context)

def get_dealers_json(request):
    dealers = [
        {"id": 1, "name": "Best Cars Chicago", "city": "Chicago", "state": "IL", "zip": "60601", "lat": "41.8781", "long": "-87.6298", "short_name": "Best Cars", "full_name": "Best Cars Chicago LLC"},
        {"id": 2, "name": "Top Autos New York", "city": "New York", "state": "NY", "zip": "10001", "lat": "40.7128", "long": "-74.0060", "short_name": "Top Autos", "full_name": "Top Autos New York LLC"},
        {"id": 3, "name": "Premier Motors LA", "city": "Los Angeles", "state": "CA", "zip": "90001", "lat": "34.0522", "long": "-118.2437", "short_name": "Premier Motors", "full_name": "Premier Motors LA LLC"},
        {"id": 4, "name": "Kansas City Motors", "city": "Kansas City", "state": "KS", "zip": "66101", "lat": "39.1141", "long": "-94.6275", "short_name": "KC Motors", "full_name": "Kansas City Motors LLC"},
        {"id": 5, "name": "Wichita Auto Group", "city": "Wichita", "state": "KS", "zip": "67202", "lat": "37.6872", "long": "-97.3301", "short_name": "Wichita Auto", "full_name": "Wichita Auto Group LLC"},
    ]
    return JsonResponse({"dealers": dealers})

def get_dealer_json(request, dealer_id):
    dealers = {
        1: {"dealer_id": 1, "name": "Best Cars Chicago", "city": "Chicago", "state": "IL", "address": "123 Main St", "zip": "60601", "lat": "41.8781", "long": "-87.6298", "short_name": "Best Cars", "full_name": "Best Cars Chicago LLC"},
        2: {"dealer_id": 2, "name": "Top Autos New York", "city": "New York", "state": "NY", "address": "456 Broadway", "zip": "10001", "lat": "40.7128", "long": "-74.0060", "short_name": "Top Autos", "full_name": "Top Autos New York LLC"},
    }
    return JsonResponse(dealers.get(dealer_id, {}))


def get_reviews_json(request, dealer_id):
    reviews = [
        {"id": 1, "dealer_id": dealer_id, "name": "John Doe", "review": "Great service!", "sentiment": "positive", "purchase_date": "2024-01-15", "car_make": "Toyota", "car_model": "Camry", "car_year": 2022},
        {"id": 2, "dealer_id": dealer_id, "name": "Jane Smith", "review": "Good experience.", "sentiment": "positive", "purchase_date": "2024-02-20", "car_make": "Honda", "car_model": "Civic", "car_year": 2023},
    ]
    return JsonResponse({"reviews": reviews})
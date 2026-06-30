from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.get_dealerships, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('registration', views.registration, name='registration'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('review/dealer/<int:dealer_id>/', views.add_review, name='add_review'),
    path('dealers/state/<str:state>/', views.get_dealers_by_state, name='get_dealers_by_state'),
    path('get_cars/', views.get_car_makes, name='get_car_makes'),
    path('analyze/', views.analyze_review, name='analyze_review'),
    path('fetchDealers/', views.get_dealers_json, name='fetch_dealers'),
    path('fetchDealer/<int:dealer_id>/', views.get_dealer_json, name='fetch_dealer'),
    path('fetchReviews/dealer/<int:dealer_id>/', views.get_reviews_json, name='fetch_reviews'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
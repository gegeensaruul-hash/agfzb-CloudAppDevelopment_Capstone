from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path(route='', view=views.get_dealerships, name='index'),
    path(route='about', view=views.about, name='about'),
    path(route='contact', view=views.contact, name='contact'),
    path(route='registration', view=views.registration, name='registration'),
    path(route='login', view=views.login_request, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='dealer/<int:dealer_id>/', view=views.get_dealer_details, name='dealer_details'),
    path(route='review/dealer/<int:dealer_id>/', view=views.add_review, name='add_review'),
    path(route='dealers/state/<str:state>/', view=views.get_dealers_by_state, name='get_dealers_by_state'),
    path(route='carmakes/', view=views.get_car_makes, name='get_car_makes'),
    path(route='analyze/', view=views.analyze_review, name='analyze_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
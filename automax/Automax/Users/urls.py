from django.urls import path
from .views import login_view, registration_view, logout_view, ProfileView,like_listing_view,inquire_listing_using_email

from Main.views import list_view, listing_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('list/', list_view, name='list'),
    path('listing/<uuid:id>/', listing_view, name='listing'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('listing/<str:id>/like/', like_listing_view, name='like_listing'),
    path('listing/<str:id>/inquire/',
         inquire_listing_using_email, name='inquire_listing'),

]


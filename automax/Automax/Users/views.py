from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, ProfileForm, LocationForm
from .models import Profile, Location
from django.utils.decorators import method_decorator
from django.views import View
from Main.models import Listing, LikedListing
from django.http import JsonResponse


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)

        # Check if the form is valid
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                # Log in the user and redirect to 'home' if authentication is successful
                login(request, user)
                messages.success(request, f"Your now looged in as {username}")
                return redirect('home')  # Replace 'home' with the correct URL name in your project

            else:
                messages.error(request, 'An error occurred trying to log you in....')

        else:
            # If the form is invalid, add an error message
            messages.error(request, 'Invalid form submission.')

        # Re-render the login page with the form and messages after POST request handling
        return render(request, 'login.html', {'login_form': login_form})

    else:  # Handles GET request
        # Render the login page with an empty form
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('main')
def registration_view(request):
    if request.method == 'POST':
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)  # Log in the user after registration
            messages.info(request, f"You are now registered as {user.username}")
            return redirect('home')  # Redirect to the home page after registration
    else:
        register_form = UserCreationForm()  # Create an empty form for GET requests
        messages.error(request, 'Please fill in the registration form.')

    return render(request, 'registration.html', {'register_form': register_form})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    def get(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(
            profile=request.user.profile).all()
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        location_form = LocationForm(instance=request.user.profile.location)
        return render(request, 'profile.html', {'user_form': user_form,
                                                      'profile_form': profile_form,
                                                      'location_form': location_form,
                                                      'user_listings': user_listings,
                                                      'user_liked_listings': user_liked_listings, })

    def post(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(
            profile=request.user.profile).all()
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        location_form = LocationForm(
            request.POST, instance=request.user.profile.location)
        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Error Updating Profile!')
        return render(request, 'profile.html', {'user_form': user_form,
                                                      'profile_form': profile_form,
                                                      'location_form': location_form,
                                                      'user_listings': user_listings,
                                                      'user_liked_listings': user_liked_listings, })

@login_required
def like_listing_view(request, id):
    listing = get_object_or_404(Listing, id=id)

    liked_listing, created = LikedListing.objects.get_or_create(
        profile=request.user.profile, listing=listing
    )

    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()

    return JsonResponse({
        'is_liked_by_user': created,
    })

@login_required
def inquire_listing_using_email(request, id):
    listing = get_object_or_404(Listing, id=id)
    try:
        emailSubject = f'{request.user.username} is interested in {listing.model}'
        emailMessage = f'Hi {listing.seller.user.username}, {request.user.username} is interested in your {listing.model} listing on AutoMax'
        send_mail(emailSubject, emailMessage, 'noreply@automax.com',
                  [listing.seller.user.email, ], fail_silently=True)
        return JsonResponse({
            "success": True,
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            "success": False,
            "info": e,
        })


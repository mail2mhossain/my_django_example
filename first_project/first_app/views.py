from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_app.forms import NewWebpageForm, UserForm, UserProfileInfoForm
from datetime import date

from django.conf import settings

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                #return HttpResponseRedirect(reverse('index'))

                print(request.path)
                #return redirect('%s?next=%s' % ('first_app/login.html', request.path))
                #return render(request, request.path, {})
                return render(request, "first_app/index.html", {})
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        print(request.path)
        #Nothing has been provided for username or password.
        return render(request, "first_app/login.html", {})


@login_required
def index(request):
    my_dict = {"insert_content":"Hello I'm from First App", "my_date":date.today()}
    return render(request, "first_app/index.html", context=my_dict)

@login_required
def newWebpage(request):
    form = NewWebpageForm()

    if request.method == "POST":
        form = NewWebpageForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error from New Webpage Form")

    return render(request, "first_app/webpage.html", {"form":form})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    #return HttpResponseRedirect('')
    return render(request, "first_app/login.html", {})

@login_required
def register(request):
    registered = False
    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # Save User Form to Database
            user = user_form.save()
            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()
            # Now we deal with the extra info!
            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']
            # Now save model
            profile.save()
            # Registration Successful!
            registered = True
        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)
    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'first_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

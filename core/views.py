from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import *
from django.core.paginator import *
from django.db.models import Q
from googleplaces import GooglePlaces, types, lang
import requests
import json
from sigma import settings
import ipinfo

"""
Hello there, I'm Tobi, 17 year old full stack developer and data scientist. I'm also a freshman at a university, chasing a degree in engineering and I am author of Sigma and team lead for the Sigma project. This code here represents the main logic of Sigma, and it's what's responsible for the workings and architecture of Sigma. 

All of this would not have been possible without help from my awesome team. I doubt they'll ever see this code right here but thank you guys for making this a reality, I love you guys very much. I really hope we win this solutions challenge and even if we don't, I don't want you guys to feel bad, we tried our best and in the end, we were able to come up with this and help solve a problem. I'm sure we'll build more amazing stuff in the future. 

For each bug and feature I either solve or create, I'll drop a dad joke.

1. What do you call a cow with no legs???
    Ground Beef(solved user auth bug)

2. Why are educated so hot???
    Cause they have more degress(Fixed mailing list bugs)

3. Why did the programmer need new glasses?
    Becaue he couldn't C# *ba dum tsss (Fixed Looping Issue With Maps API)

4. Why was 6 afraid of 7?
    Because 7, 8, 9(Fixed styling issue with maps)

5. What do you call a cow with no legs?
    Ground BEEF!!!!!!
"""

# -------------- Auth Views ------------ #


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def doctor(request):
    doctor = Doctor.objects.filter(approved="yes")
    context = {
        'doctor' : doctor
    }
    return render(request, 'doctor.html', context)

@login_required
def my_appointments(request):
    appointment = Appointment.objects.filter(booker=request.user)
    context = {
        'appointments' : appointment
    }
    return render(request, 'my-appointments.html', context)

@login_required
def doc_profile(request, pk):
    user_profile = Profile.objects.get(owner=request.user)
    user_object= Doctor.objects.get(phone_number=pk)
    doctor = user_object.name
    context = {
        'user_profile' : user_profile,
        'user_object' : user_object,
    }
    username = request.user

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_address = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
        ctx = {
            'user' : username,
            'email' : email_address,
            'message' : message,
            'first_name' : first_name,
            'last_name' : last_name,
            'subject' : subject
        }
        # message = get_template('appoint_mail.html').render(ctx)
        msg = EmailMessage(
            'Appointment Booking',
            f'''Hello there {user_object.name}, you have been booked for an appointment by {user_profile.owner} on Sigma. 
            Here is an overview of the person who booked the appointment.
            Email Address:
            {email_address}
            First Name:
            {first_name}
            Last Name:
            {last_name}
            Message:
            {message}
            ''',
            'Sigma',
            [user_object.email],
        )
        msg.content_subtype ="html"# Main content is now text/html
        msg.send()
        messages.info(request, 'Your appointment has been booked successfully, the appointed doctor will send you a message in regards to booking time as soon as possible.')
        Appointment.objects.create(booker=request.user, first_name=first_name, last_name=last_name, email_address=email_address, message=message, doctor=Doctor.objects.get(name=user_object.name))
    
    return render(request, 'doctor-profile.html', context)

@login_required
def courses(request):
    return render(request, 'courses.html')

@login_required
def self_health(request):
    courses = Course.objects.filter(category="Self Health")
    context = {
        'course' : courses
    }
    return render(request, 'category.html', context)

@login_required
def mental_health(request):
    courses = Course.objects.filter(category="Mental Health")
    context = {
        'course' : courses
    }
    return render(request, 'category.html', context)

@login_required
def care_giving(request):
    courses = Course.objects.filter(category="Care Givnig")
    context = {
        'course' : courses
    }
    return render(request, 'category.html', context)

@login_required
def psycology(request):
    courses = Course.objects.filter(category="Psycology")
    context = {
        'course' : courses
    }
    return render(request, 'category.html', context)

@login_required
def dental_health(request):
    courses = Course.objects.filter(category="Dental Health")
    context = {
        'course' : courses
    }
    return render(request, 'category.html', context)

@login_required
def physical_fitness_and_exercise(request):
    courses = Course.objects.filter(category="Physical Fitness and Exercise")
    context = {
        'course' : courses
    }
    return render(request, 'category.html', context)

@login_required
def det(request, slug):
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    lectures = course.lecture_set.all().order_by('serial_number')


    if serial_number is None:
        serial_number = 1
    lecture = Lecture.objects.get(serial_number = serial_number, course = course)



    context = {
        'course' : course,
        'lecture' : lecture,
        'lectures' : lectures,
        'title' : course

    }
    return render(request, 'det.html', context)

@login_required
def first_aid(request):
    first_aid = FirstAid.objects.all()
    context = {
        'first_aid' : first_aid
    }
    return render(request, 'first_aid.html', context)

@login_required
def first_det(request, pk):
    first_aid = FirstAid.objects.get(slug=pk)
    context = {
        'first_aid' : first_aid
    }
    return render(request, 'first_detail.html', context)

@login_required
def hospital_finder(request):
    access_token = settings.IP_ACCESS_TOKEN
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    lat = details.latitude
    lon = details.longitude
    # Use your own API key for making api request calls
    API_KEY = settings.GOOGLE_API_KEY
    
    # Initialising the GooglePlaces constructor
    google_places = GooglePlaces(API_KEY)
    
    # call the function nearby search with
    # the parameters as longitude, latitude,
    # radius and type of place which needs to be searched of 
    # type can be HOSPITAL, CAFE, BAR, CASINO, etc
    # send_url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={settings.GOOGLE_API_KEY}'
    # r = requests.get(send_url)
    # j = json.loads(r.text)
    # print(j)
    # lat = j['location']['lat']
    # lon = j['location']['lng']
    # print(lat)
    # print(lon)
    query_result = google_places.nearby_search(
            # lat_lng ={'lat': 46.1667, 'lng': -1.15},
            lat_lng ={'lat':lat, 'lng':lon},
            radius = 50000,
            # types =[types.TYPE_HOSPITAL] or
            # [types.TYPE_CAFE] or [type.TYPE_BAR]
            # or [type.TYPE_CASINO])
            types =[types.TYPE_HOSPITAL])
    
    # If any attributions related 
    # with search results print them
    if query_result.has_attributions:
        print (query_result.html_attributions)
    
    
    # Iterate over the search results
    result_list = []
    for place in query_result.places:
        result_dict = {
            'h' :place.get_details(),
            'place' : place.name,
            'dets' :  place.get_details(),
            'lat' : place.geo_location['lat'],
            'lng' : place.geo_location['lng'],
            'phone_number' : place.local_phone_number,
            'vicinity' : place.vicinity,
        }
        result_list.append(result_dict)


        context = {
            'results' : result_list
        }

        # print(place)
        # place.get_details()
        # print (place.name)
        # print("Latitude", place.geo_location['lat'])
        # print("Longitude", place.geo_location['lng'])
        # print(place.local_phone_number)
        # print()
    return render(request, 'hospital-finder.html', context)

@login_required
def latest_news(request):
    news = LatestNews.objects.filter(publish="yes")
    context = {
        'news' : news
    }
    return render(request, 'latest-news.html', context)

@login_required
def latest_det(request, pk):
    latest = LatestNews.objects.get(slug=pk)
    context = {
        'latest' : latest

    }
    return render(request, 'latest-det.html', context)

@login_required
def profile(request):
    user_profile = Profile.objects.get(owner=request.user)
    if request.method == "POST":
        phone_number = request.POST['phone_number']
        blood_group = request.POST['blood_group']
        allergies = request.POST['allergies']
        address = request.POST['address']
        nationality = request.POST['nationality']
        medical_history = request.POST['medical_history']
        about_me = request.POST['about_me']
        how_did_you_hear_about_us = request.POST['how']
        what_will_you_use_sigma_for = request.POST['join_reason']
        medical_conditions = request.POST['conditions']
        genotype = request.POST['genotype']


        user_profile.phone_number = phone_number
        user_profile.blood_group = blood_group
        user_profile.allergies = allergies
        user_profile.address = address
        user_profile.nationality = nationality
        user_profile.medical_history = medical_history
        user_profile.about_me = about_me
        user_profile.how_did_you_hear_about_us = how_did_you_hear_about_us
        user_profile.what_will_you_use_sigma_for = what_will_you_use_sigma_for
        user_profile.medical_conditions = medical_conditions
        user_profile.genotype = genotype
        user_profile.save()
        return redirect("home")
    
    context = {
    'user_profile' : user_profile
    }   
    
    return render(request, 'profile.html', context)

@login_required
def cont(request):
    if Profile.objects.filter(owner=request.user).exists():
        return redirect("home")
    else:
        user_model = User.objects.get(username=request.user)
        new_profile = Profile.objects.create(owner=user_model, id_user=user_model.id)
        new_profile.save()
        ctx = {
            'user' : user_model.username
        }
        message = get_template('mail.html').render(ctx)
        msg = EmailMessage(
            'Welcome to Sigma',
            message,
            'Paradoxx',
            [user_model.email],
        )
        msg.content_subtype ="html"# Main content is now text/html
        msg.send()
    return render(request, 'next.html')

# -------------- Auth Views End --------- #




# ----------- No Auth Views ------------ #
def index(request):
    return render(request, 'index.html')

def login(request):
    user = request.user

    if user.is_authenticated:
        return redirect(home)

    context = {
        'title' : 'Login',
    }
    if request.method == 'POST':
        username = request.POST['username'] #Requesting Username
        password = request.POST['password'] #Requesting Password
    
        user = auth.authenticate(username=username, password=password)

        if user is not None: #Cheking If User Exists in the database
            auth.login(request, user) # Logs in User
            return redirect('home') # Redirects to home view
        else:
            messages.info(request, 'Invalid Username or Password') #Conditional Checking if credentials are correct
            return redirect('login')#Redirects to login if invalid

    else:
        return render(request, 'login.html', context)


def register(request):
    user = request.user

    if user.is_authenticated:
        return redirect("home")
    context = {
        'title' : 'Sign Up',
    }
    if request.method == 'POST':
        #Requesting POST data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #End of POST data request

        #Condition is executed if both passwords are the same
        if password == password2:
            if User.objects.filter(email=email).exists(): #Checking databse for existing data
                messages.info(request, "This email is already in use")#Returns Error Message
                return redirect(register)
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            #Else condition executed if the above conditions are not fulfilled    
            else:
                ctx = {
                    'user' : username
                }
                message = get_template('mail.html').render(ctx)
                msg = EmailMessage(
                    'Welcome to Paradoxx',
                    message,
                    'Paradoxx',
                    [email],
                )
                msg.content_subtype ="html"# Main content is now text/html
                msg.send()
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name )
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)#Logs in USER



            #Create user model and redirect to edit-profile
            return redirect('cont')#Rediects to specified page once condition is met
        else:
            messages.info(request, "Passwords do not match")
            return redirect("register")

    else:
        return render(request, 'register.html', context)

# ------------ No Auth Views End -------- #




# Create your views here.

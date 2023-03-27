from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import *
from django.core.paginator import *
from django.db.models import Q


"""
Hello there, I'm Tobi, 17 year old full stack developer and data scientist. I'm also a freshman at a university, chasing a degree in engineering and I am author of Sigma and team lead for the Sigma project. This code here represents the main logic of Sigma, and it's what's responsible for the workings and architecture of Sigma. 

All of this would not have been possible without help from my awesome team. I doubt they'll ever see this code right here but thank you guys for making this a reality, I love you guys very much. I really hope we win this solutions challenge and even if we don't, I don't want you guys to feel bad, we tried our best and in the end, we were able to come up with this and help solve a problem. I'm sure we'll build more amazing stuff in the future. 

For each bug and feature I either solve or create, I'll drop a dad joke.

1. What do you call a cow with no legs???
    Ground Beef(solved user auth bug)

2. Why are educated so hot???
    Cause they have more degress(Fixed mailing list bugs)

3. 
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
def profile(request):
    return redirect(request, 'profile.html')

@login_required
def appointment(request):
    return render(request, 'appointment.html')

@login_required
def doctor(request):
    doctor = Doctor.objects.filter(approved="yes")
    context = {
        'doctor' : doctor
    }
    return render(request, 'doctor.html', context)

@login_required
def doc_profile(request, pk):
    user_profile = Profile.objects.get_or_create(owner=request.user)
    user_object= Doctor.objects.get(phone_number=pk)
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
        ctx = {
            'user' : username,
            'email' : email_address,
            'message' : message,
            'first_name' : first_name,
            'last_name' : last_name,
        }
        message = get_template('appoint_mail.html').render(ctx)
        msg = EmailMessage(
            'Appointment Booking',
            message,
            'Sigma',
            [user_object.email],
        )
        msg.content_subtype ="html"# Main content is now text/html
        msg.send()
        messages.info(request, 'Your appointment has been booked successfully, the appointed doctor will send you a message in regards to booking time as soon as possible.')
        Appointment.objects.create(booker=request.user, first_name=first_name, last_name=last_name, email_address=email_address, message=message)
    
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
    first_aid = FirstAid.objects.filter(approved="yes")
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
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(owner=user_model, id_user=user_model.id)
            new_profile.save()
            return redirect('edit-profile')#Rediects to specified page once condition is met
        else:
            messages.info(request, "Passwords do not match")
            return redirect("register")

    else:
        return render(request, 'register.html', context)

# ------------ No Auth Views End -------- #




# Create your views here.

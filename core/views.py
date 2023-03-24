from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import *
from django.core.paginator import *
from django.db.models import Q


# -------------- Auth Views ------------ #
def home(request):
    return render(request, 'home.html')
# -------------- Auth Views End --------- #

# ----------- No Auth Views ------------ #
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    # user = request.user

    # if user.is_authenticated:
    #     return redirect("home")
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
                # ctx = {
                #     'user' : username
                # }
                # message = get_template('mail.html').render(ctx)
                # msg = EmailMessage(
                #     'Welcome to Paradoxx',
                #     message,
                #     'Paradoxx',
                #     [email],
                # )
                # msg.content_subtype ="html"# Main content is now text/html
                # msg.send()
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

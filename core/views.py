from django.shortcuts import render




# ----------- No Auth Views ------------ #
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
# ------------ No Auth Views End -------- #


# -------------- Auth Views ------------ #
def home(request):
    return render(request, 'home.html')
# -------------- Auth Views End --------- #

# Create your views here.

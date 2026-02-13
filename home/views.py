from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
# admin user password: DIPALI**123%
def index(request):
    context = {
        "variable1": "this is sent",
        "variable2": "Dipali is great"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("This is about page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def service(request):
    return render(request, 'service.html')
    # return HttpResponse("This is service page")

def contact(request):
    print("Contact view loaded")  # 🔍 This should always show, even on GET

    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        feedback = request.POST.get('feedback')

        print(f"Form submitted: {name}, {email}, {feedback}")  # 🔍 Debug log

        contact = Contact(
            name=name,
            email=email,
            password=password,
            feedback=feedback,
            date=datetime.today()
        )
        contact.save()
        messages.success(request, "Your details has been sent.")
        return render(request, 'contact.html', {'message': 'Form submitted successfully.'})
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        context = {}

        if User.objects.filter(username=username).exists():
            context['username_error'] = "Username already taken"
            return render(request, 'signup.html', context)
            return redirect('/signup')
        
        if User.objects.filter(email=email).exists():
            context['email_error'] = "Email already registered."
            return render(request, 'signup.html', context)
            return redirect('/signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created succesfully! You can now log in")
        context['redirect_to_login'] = True
        return render(request, 'signup.html', context)
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

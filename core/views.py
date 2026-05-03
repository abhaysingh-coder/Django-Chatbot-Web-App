import uuid
from.models import *
from .chatbot import *
from .models import User
from django.db import IntegrityError
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def reset_session(request):
    request.session["messages"] = []
    request.session.modified = True
    return redirect('home')

def login(request):
    if request.method == "POST":
        role = request.POST.get("role","").strip().lower()
        email = request.POST.get("username","").strip().lower()
        password = request.POST.get("password")
        user = User.objects.filter(email=email, role=role).first()
        if user and user.check_password(password):
            auth_login(request, user)
            if role == "user":
                return redirect('user_page')
            elif role == "customer":
                return redirect('home')
        return render(request, 'Login_Page.html', {"error_message": "Invalid email, role or password"})
    return render(request, 'Login_Page.html')

def signup(request):
    if request.method == "POST":
        role = request.POST.get("role")
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            User.objects.create_user(username=str(uuid.uuid4()), email=username, password=password, role=role)
        except IntegrityError:
            return render(request, 'Signup.html', {"error_message": "* Account already exists for this role"})
        return redirect('login')
    return render(request, 'Signup.html')

def forget(request):
    if request.method == "POST":
        role = request.POST.get("role", "").strip().lower()
        username = request.POST.get("username", "").strip().lower()
        password = request.POST.get("password")
        user = User.objects.filter(role=role, email=username).first()
        if user:
            user.set_password(password)  # hash properly
            user.save()
            return redirect('login')
        return render(request, 'forget.html', {"error_message": "* Email not found"})
    return render(request, 'forget.html')

@login_required
def user_page(request):
    return render(request, 'user.html',{'data':ChatMessage.objects.all()})

@login_required
def home(request):
    if "messages" not in request.session:
        request.session["messages"] = []
    messages = request.session["messages"]
    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()
        if user_message:
            messages = messages + [{"sender": "user", "text": user_message}]
            msg = user_message.lower()
            if "hello" in msg or "hi" in msg:
                reply = "Hello! How can I help you?"
            elif "how are you" in msg:
                reply = "I'm doing great 😄"
            elif "bye" in msg:
                reply = "Goodbye! Have a nice day!"
            else:
                reply = prediction(msg, 'Intent')
                user_identity = f"{request.user.role}_{request.user.email}"
                ChatMessage.objects.create(User_Identity=user_identity, Flags=prediction(msg, 'Flags'), Utterance=user_message, Category=prediction(msg, 'Category'), Intent=reply)
            messages = messages + [{"sender": "bot", "text": reply}]
        request.session["messages"] = messages
        request.session.modified = True
    return render(request, 'home.html', {"messages": messages})
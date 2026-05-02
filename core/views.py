from django.shortcuts import render, redirect
from.models import *
from .chatbot import *

# Create your views here.
def home(request):
    chatmessage = ChatMessage.objects.all()
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
                reply = prediction(msg, 'Chatbot')
            messages = messages + [{"sender": "bot", "text": reply}]
        request.session["messages"] = messages
        request.session.modified = True
    return render(request, 'home.html', {"messages": messages})

def reset_session(request):
    request.session.clear() 
    request.session.flush() 
    return redirect('home')
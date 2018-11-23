from django.shortcuts import render, redirect
from .models import message
from django.contrib.auth.models import User
# from django.contrib import auth
# Create your views here.
def dashboard(request):
    messages_sent = message.objects.order_by('-time').filter(sender__exact=request.user.username)
    messages_received = message.objects.order_by('-time').filter(receiver__exact=request.user.username)
    total = len(messages_sent) + len(messages_received)
    return render(request, 'chats/dashboard.html',{'sent':messages_sent, 'received':messages_received, 'total':total})

def search(request):
    return render(request, 'chats/search.html')

def send(request):
    if request.method == 'POST':
        receiverUsername = request.POST['username']
        receiverMessage = request.POST['message']
        thisUser = request.user.username
        if not User.objects.filter(username=receiverUsername).exists():
            return redirect('dashboard')
            #show some kind of error saying that the user doesn't exist
        else:
            message_text = message(sender=thisUser, receiver=receiverUsername, body=receiverMessage)
            message_text.save()
            return redirect('dashboard')

def chat(request, receiver_id):
    return render(request, 'chats/chat.html')

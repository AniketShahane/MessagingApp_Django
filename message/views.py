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
    results = message.objects.order_by('-time')
    is_filtered = 0
    if 'messenger_name' in request.GET:
        messenger_name = request.GET['messenger_name']
        if messenger_name:
            results = results.filter(sender=messenger_name, receiver=request.user.username)
            is_filtered = 1

    if 'message_content' in request.GET:
        message_content = request.GET['message_content']
        if message_content:
            results = results.filter(body__icontains=message_content)
            is_filtered = 1

    return render(request, 'chats/search.html', {'results':results, 'is_filtered':is_filtered})


def send(request):
    if request.method == 'POST':
        try:
            receiverSenderMessage = request.POST['andagundu']
        except:
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



def chat(request, receiver_username):
    sent_messages = message.objects.order_by('-time').filter(sender=request.user.username,receiver=receiver_username)
    received_messages = message.objects.order_by('-time').filter(sender=receiver_username, receiver=request.user.username)
    s = 0
    #tracks the index of the sent messages
    r = 0
    #tracks the index of the received messages
    querySet = []
    while(s < len(sent_messages) and r < len(received_messages)):
        if(sent_messages[s].time > received_messages[r].time):
            querySet.append({'msg':sent_messages[s],'sent':1})
            s+=1
        else:
            querySet.append({'msg':received_messages[r],'sent':0})
            r+=1
    if (s < len(sent_messages)):
        while(s!=len(sent_messages)):
            querySet.append({'msg':sent_messages[s],'sent':1})
            s+=1
    elif (r < len(received_messages)):
        while(r!=len(received_messages)):
            querySet.append({'msg':received_messages[r],'sent':0})
            r+=1
    querySet.reverse()
    return render(request, 'chats/chat.html', {'chats':querySet, 'friend':receiver_username})

def chatbox(request, receiver_user):
    if request.method == 'POST':
        sent_messages = message.objects.order_by('-time').filter(sender=request.user.username,receiver=receiver_user)
        received_messages = message.objects.order_by('-time').filter(sender=receiver_user, receiver=request.user.username)
        s = 0
        #tracks the index of the sent messages
        r = 0
        #tracks the index of the received messages
        querySet = []
        while(s < len(sent_messages) and r < len(received_messages)):
            if(sent_messages[s].time > received_messages[r].time):
                querySet.append({'msg':sent_messages[s],'sent':1})
                s+=1
            else:
                querySet.append({'msg':received_messages[r],'sent':0})
                r+=1
        if (s < len(sent_messages)):
            while(s!=len(sent_messages)):
                querySet.append({'msg':sent_messages[s],'sent':1})
                s+=1
        elif (r < len(received_messages)):
            while(r!=len(received_messages)):
                querySet.append({'msg':received_messages[r],'sent':0})
                r+=1
        querySet.reverse()

        message_receiver = request.POST['send_message']
        new_message = message(sender=request.user.username, receiver=receiver_user, body=message_receiver)
        new_message.save()

        querySet.append({'msg':new_message, 'sent':1})
        return redirect('/messages/chat/'+receiver_user,{'chats':querySet, 'friend':receiver_user})

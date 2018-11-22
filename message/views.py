from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'chats/dashboard.html')

def search(request):
    return render(request, 'chats/search.html')

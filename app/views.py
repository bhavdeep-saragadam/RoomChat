from django.shortcuts import render, redirect

# Create your views here.

def start(request):
        if request.method == 'POST':
                username = request.POST.get('name')
                response =  render(request, 'main.html', {'username': username})
                response.set_cookie('name', username)

        

        return render(request, 'login.html')


def home(request):
        username = request.POST.get('name')

        
        return render(request, 'main.html', {'username': username})


def room1(request):

        username = request.POST.get('name')

        username = request.COOKIES.get(username)

        return render(request, 'room1.html', {'username': username})



def room2(request):

        username = request.POST.get('name')

        username = request.COOKIES.get(username)

        return render(request, 'room2.html', {'username': username})


def room3(request):

        username = request.POST.get('name')

        username = request.COOKIES.get(username)

        return render(request, 'room3.html', {'username': username})


def room4(request):

        username = request.POST.get('name')

        username = request.COOKIES.get(username)

        return render(request, 'room4.html', {'username': username})


def room5(request):

        username = request.POST.get('name')

        username = request.COOKIES.get(username)

        return render(request, 'room5.html', {'username': username})
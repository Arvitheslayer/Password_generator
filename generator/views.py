from django.shortcuts import render
from django.http import HttpResponse
from random import *
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):

    characters = list("qwertyuiopasdfghjklzxcvbnm")

    if request.GET.get('uppercase'):
        characters.extend(list("QWERTYUIOPASDFGHJKLZXCVBNM"))

    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_+-="))

    if request.GET.get('numbers'):
        characters.extend(list("0123456789"))

    lengh = int(request.GET.get('lenght', 12))

    thepassword = ''

    for x in range(lengh):
        thepassword += choice(characters)

    return render(request,'generator/password.html', {'password':thepassword})
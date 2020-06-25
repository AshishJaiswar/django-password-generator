from django.shortcuts import render
from random import choice
# Create your views here.

def index(request):
    return render(request, "generator/index.html")

def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('special_characters'):
        characters.extend(list("!@#$%^&*()_"))
    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))
    thepassword = ''
    for x in range(length):
        thepassword += choice(characters)
    return render(request, "generator/password.html", {'password':thepassword})


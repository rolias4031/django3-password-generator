from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about_page(request):
    return render(request, 'generator/about.html')

def password(request):

    the_password = ''
    characters = list(string.ascii_lowercase)

    if request.GET.get('Uppercase'):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*?'))

    length = int(request.GET.get('length', 21))

    for i in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':the_password, 'characters':characters})

from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render

from . import forms

def index(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            return render(request,'CrazyPasswordApp/success.html')
    return render(request, 'CrazyPasswordApp/index.html', context={'form': form})

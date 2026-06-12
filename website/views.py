from django.shortcuts import render, redirect
from .models import Pray
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def pray(request):

    if request.method == 'POST':
        # Grab data from the form using the 'name' attributes
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Save the data to the database
        Pray.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        
       # Add the success message here
        messages.success(request, f"Thank you {first_name}, your request has been sent successfully!")
        
        # Redirect back to the form page safely
        return redirect('pray')

    return render(request, 'pray.html')


def serve(request):
    return render(request, 'serve.html')


def give(request):
    return render(request, 'give.html')


def learn(request):
    return render(request, 'learn.html')


def vision(request):
    return render(request, 'vision.html')
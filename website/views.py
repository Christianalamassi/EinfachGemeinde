from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pray


def home(request):
    return render(request, 'home.html')


def pray(request):
    if request.method == 'POST':
        # Grab data from the form using the 'name' attributes
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            # raise Exception("Testing my error style!")
            # Save the data to the database
            Pray.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            # Success message
            messages.success(request, f"Thank you {first_name}, your request has been sent successfully!")
        
        except Exception as e:
            # Failure message if something goes wrong
            messages.error(request, "Oops! Something went wrong. Please try submitting your request again.")

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


def error_404_view(request, exception):
    # This points to wherever your 404 html file is
    return render(request, '404.html', status=404)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Pray
from django.contrib.auth.models import User


def home(request):
    # 🛠️ TEMPORARY LIVE SUPERUSER GENERATOR
    # This automatically checks if an admin exists. If not, it creates it silently!
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="einfachgemeinde", 
            password="EinfachGeminde1230" # <-- CHANGE THIS PASSWORD HERE!
        )
        print("🎉 SUCCESS: Live admin user created seamlessly!")

    if request.method == 'POST':
        # ... (rest of your form code continues exactly the same below)
        return render(request, 'home.html')


def pray(request):
    if request.method == 'POST':
        # 1. Grab all data fields from the incoming POST form
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')      # Captures the optional phone number
        message = request.POST.get('message')  # Captures the text area answers

        try:
            # 2. Save the dataset securely to your database
            Pray.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                message=message
            )
            
            # 3. Construct the email structural payload for the administrator
            subject = f"🙏 New Prayer/Vision Submission from {first_name} {last_name}"
            
            email_body = f"""
                Hello Admin,

                A new response form has been submitted on the EinfachGemeinde portal.

                --- SUBMISSION DETAILS ---
                Name: {first_name} {last_name}
                Email: {email}
                Phone: {phone if phone else 'Not provided'}

                Message / Vision Responses:
                {message if message else 'No message text provided.'}
                --------------------------

                You can review or manage this submission inside your Django Admin Dashboard.
                """
            
            # 4. Attempt to trigger the email engine
            send_mail(
                subject=subject,
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['einfachgemeindeberlin@gmail.com'], # <-- Email here when going live!
                fail_silently=False,
            )

            # 5. Success alert trigger for the user interface
            messages.success(request, f"Thank you {first_name}, your request has been sent successfully!")
        
        except Exception as e:
            # Explicit debug crash log cleanly printed to your server terminal output lines
            print("\n🚨 DATABASE/EMAIL EXCEPTION ERROR:", str(e), "\n")
            messages.error(request, "Oops! Something went wrong. Please try submitting your request again.")

        # Always redirect safely to prevent duplicate form submissions if the user refreshes
        return redirect('pray')

    # Standard GET handling when loading the page fresh
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
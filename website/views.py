from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def pray(request):
    return render(request, 'pray.html')


def serve(request):
    return render(request, 'serve.html')


def give(request):
    return render(request, 'give.html')


def learn(request):
    return render(request, 'learn.html')


def vision(request):
    return render(request, 'vision.html')
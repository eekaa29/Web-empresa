from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html" )


def about_us(request):
    return render(request, "core/about.html" )


def visit_us(request):
    return render(request, "core/store.html" )


def contact(request):
    return render(request, "core/contact.html" )




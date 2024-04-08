from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>This is Home Page</h1>")


def about(request):
    return HttpResponse("<h1>This is About Page</h1>")


def services(request):
    return HttpResponse("<h1>This is Services Page</h1>")


def contact(request):
    return HttpResponse("<h1>This is Contact Page</h1>")

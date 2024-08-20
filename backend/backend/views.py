from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Server up and Running!</h1>")

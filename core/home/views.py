from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Hey Keerthana, Welcome to the World Of Django")
    return render(request, 'home/index.html')

def success_page(request):
    return HttpResponse("<h1>This is the Success Page</h1>")
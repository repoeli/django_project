from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    # Render the 'about' page
    return HttpResponse('about/about.html')
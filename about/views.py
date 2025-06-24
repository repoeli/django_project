from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_me(request):
    # Render the 'about' page
    return HttpResponse('This would be the about page. You can add more content here as needed.')
from django.shortcuts import render
from .models import Job

# Create your views here.
def peter(request):
    # if refererenced, return html file
    return render(request, 'jobs/peter.html')

# Create your views here.
def showHome(request):
    # gets all objects
    jobs = Job.objects
    # if refererenced, return html file
    return render(request, 'jobs/home.html',{'jobs':jobs})
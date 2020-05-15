from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):

    #dests = Destination.objects.all()

    dests = Destination.objects.order_by('name') # if you wish to display the content orderby
    context = {'dests': dests}
    return render(request,'index.html',context)

def contact(request):

    return render(request,'contact.html')
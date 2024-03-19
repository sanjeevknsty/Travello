from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

   full_dest=Destination.objects.all()

   return render(request,'index.html',{'full_dest':full_dest})
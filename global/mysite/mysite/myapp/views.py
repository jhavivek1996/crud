from django.shortcuts import *
from .forms import *
# from .models import *

def insert(request):
	if request.method=="POST":
		form = globalform(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Success")
	else:
		form = globalform()
		return render(request,"register.html",{'form':form})

def show(request):
	shown=globalform.objects.all()
	return render(request,"show.html",{'shown':shown})
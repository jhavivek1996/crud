from django.shortcuts import *
from .models import *
from .forms import *

def insert(request):
	if request.method=="POST":
		insert_form=gameform(request.POST)
		if insert_form.is_valid:
			try:
				insert_form.save()
				return HttpResponse("Succeed")


			except:
				pass
	else:
		insert_form=gameform()
		return render(request, "index.html",{'insert_form':insert_form})

def show(request):
	show_model=game.objects.all()
	return render(request,"show.html",{'show_model':show_model})

def destory(request,id):
	remove_game=game.objects.get(id=id)
	remove_game.delete()
	return redirect('/show')

# 

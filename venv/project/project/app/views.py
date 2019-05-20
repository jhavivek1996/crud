from django.shortcuts import *
from .models import *
from .forms import EmployeeForm

def insert(request):
	if request.method=="POST":
		form = EmployeeForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return HttpResponseRedirect("/show")
			except:
				pass
	else:
		form = EmployeeForm()
		return render(request,'index.html',{'form':form})


def show(request):
 	forms = Employee.objects.all()  
 	return render(request,"show.html",{'forms':forms})

 

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,"edit.html", {'employee':employee})
    


def update(request, id=None):  
    update_model = Employee.objects.get(id=id)
    if request.method== "POST":
    	update_form=EmployeeForm(request.POST,instance=update_model)
    	if update_form.is_valid():
    		update_form.save()
    		return redirect('show')
    else:
    	update_form=EmployeeForm(instance=update_model)
    return render(request, 'edit_data.html',{'update_form':update_form})

	  


def destroy(request,id):
	destroy_form=Employee.objects.get(id=id)
	destroy_form.delete()
	return redirect('/show')
	




# def sellerTableUpdate(request,id=None):
# 	sellerbookEdit=SellerAddBook.objects.get(id=id)
# 	if request.method=="POST":
# 		form = sellerForm(request.POST,request.FILES,instance=sellerbookEdit)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('sellerTable')
# 	else:
# 		sellerbookupdate = sellerForm(instance=sellerbookEdit)
# 	return render(request, 'sellerEditBookPage.html', {'sellerbookupdate': sellerbookupdate})


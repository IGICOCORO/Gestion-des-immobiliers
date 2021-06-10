from django.urls import reverse_lazy
from django.shortcuts import  render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth import login as auth_login ,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from    .forms  import *
from .models import *


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="loyer/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="loyer/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")


def home(request):
	listing = Office.objects.all()
	context = { 'listing': listing}
	return render(request,'loyer/index.html',context)


def office(request):
	tenants = Locataire.objects.all()
	offices = Office.objects.all()
	context = {'offices': offices, 'tenants':tenants}
	return render(request,'loyer/office.html',context)


def tenant(request):
	tenants = Locataire.objects.all()
	context = { 'tenants': tenants}
	return render(request,'loyer/tenant.html',context)

def calendar(request):
	calender = Calender.objects.all()
	context = { 'calender': calender}
	return render(request,'loyer/calendar.html',context)


# --------------------------office------------------------------
# @login_required 
def office_create(request, template_name='loyer/officeform.html'):
	form = OfficeForm()
	if request.method == 'POST':
		form = OfficeForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			form.save()
			return redirect('/office')
	else:
		form = OfficeForm()
	return render(request,template_name, {'form': form})


def office_update(request, id, template_name='loyer/officeform.html'):
	post= get_object_or_404(Office, id=id)
	form = OfficeForm(request.POST, request.FILES, instance=post)
	if form.is_valid():
		form.save()
		return redirect('office')
	return render(request, template_name, {'form':form})

def office_detail(request, id, template_name = 'loyer/officedetail.html'):
	office = get_object_or_404(Office, id=id)
	return render(request, template_name, {'office':office})

def  office_destroy(request, id):  
	post = Office.objects.get(id=id)  
	post.delete()  
	return redirect("/office")  


# ---------------------------Tenant------------------------------------------
def tenant_create(request, template_name='loyer/tenantform.html'):
	form = LocataireForm()
	if request.method == 'POST':
		form = LocataireForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			form.save()
			return redirect('/tenant')
	else:
		form = LocataireForm()
	return render(request,template_name, {'form': form})

def tenant_update(request, id, template_name='loyer/tenantform.html'):
	post= get_object_or_404(Locataire, id=id)
	form = LocataireForm(request.POST, request.FILES, instance=post)
	if form.is_valid():
		form.save()
		return redirect('/tenant')
	return render(request, template_name, {'form':form})



def  tenant_destroy(request, id):  
	post = Locataire.objects.get(id=id)  
	post.delete()  
	return redirect("/tenant")  



# -----------------------------calendar---------------------------------------------------
def calender_create(request, template_name='loyer/calendarform.html'):
	form = CalenderForm()
	if request.method == 'POST':
		form = CalenderForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			form.save()
			return redirect('/calendar')
	else:
		form = CalenderForm()
	return render(request,template_name, {'form': form})


def calender_update(request, id, template_name='loyer/calendarform.html'):
	post= get_object_or_404(Calender, id=id)
	form = CalenderForm(request.POST, request.FILES, instance=post)
	if form.is_valid():
		form.save()
		return redirect('/calendar')
	return render(request, template_name, {'form':form})



def  calender_destroy(request, id):  
	post = Calender.objects.get(id=id)  
	post.delete()  
	return redirect("/calendar")  


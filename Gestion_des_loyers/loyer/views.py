from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth import login as auth_login ,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from    .forms  import *
from .models import *
# new features
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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
	all = Office.objects.filter(is_available=True)
	# context = { 'all': all}
	page = request.GET.get('page', 1)

	paginator = Paginator(all, 9)
	try:
		listing = paginator.page(page)
	except PageNotAnInteger:
		listing = paginator.page(1)
	except EmptyPage:
		listing = paginator.page(paginator.num_pages)

	return render(request,'loyer/index.html',{ 'listing': listing })


def office(request):
	tenants = Locataire.objects.all()
	offices = Office.objects.all()
	context = {'offices': offices, 'tenants':tenants}
	return render(request,'loyer/office.html',context)


def tenant(request):
	# tenants = Locataire.objects.all()
	# context = { 'tenants': tenants}
	search_post = request.GET.get('search')

	if search_post:
		tenants =Locataire.objects.filter(Q(first_name__icontains=search_post) or Q(last_name__icontains=search_post))
		context = { 'tenants': tenants}
	else:
	# If not searched, return default tenants
		tenants =Locataire.objects.all()#.order_by("-date_created")
		context = { 'tenants': tenants}
	return render(request,'loyer/tenant.html', context)


def calendar(request):
	search_post = request.GET.get('search')
	if search_post:
		tenants =calender = Calender.objects.filter(Q(start_rent_date__icontains=search_post))
		context = { 'calender': calender}
	else:
	# If not searched, return default tenants
		tenants =calender = Calender.objects.all()#.order_by("-date_created")
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

def search_view(request):
	# whatever user write in search box we get in query
	query = request.GET['query']
	offices=Office.objects.all().filter(first_name__icontains=query, last_name__icontains=query)
	if 'office_ids' in request.COOKIES:
		office_ids = request.COOKIES['office_ids']
		counter=office_ids.split('|')
		product_count_in_cart=len(set(counter))
	else:
		product_count_in_cart=0

	# word variable will be shown in html when user click on search button
	word="Searched Result :"

	if request.user.is_authenticated:
		return render(request,'loyer/tenant.html',{'offices':offices,'word':word,'product_count_in_cart':product_count_in_cart})
	return render(request,'loyer/tenant.html',{'offices':offices,'word':word,'product_count_in_cart':product_count_in_cart})


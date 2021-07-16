from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from    .forms  import *
from .models import *
from django.contrib.auth.decorators import login_required,user_passes_test
# new features
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import user_passes_test


def is_locatire(user):
	return user.groups.filter(name='LOCATAIRE').exists()

@login_required 
def dashboard(request):
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

@login_required(login_url='is_locatire') 
def office(request):
	tenants = Locataire.objects.get(user_id=request.user.id)
	offices = Office.objects.all()
	context = {'offices': offices, 'tenants':tenants}
	return render(request,'loyer/office.html',context)

# @login_required(login_url='is_superuser') 
@login_required
# @user_passes_test(lambda u: u.is_superuser)
@user_passes_test(lambda u: u.is_superuser)
def tenant(request):
	# tenants = Locataire.objects.all()
	# context = { 'tenants': tenants}
	search_post = request.GET.get('search')

	if search_post:
		tenants =Locataire.objects.filter(Q(first_name__icontains=search_post) or Q(last_name__icontains=search_post))
		context = { 'tenants': tenants}
	else:
	# If not searched, return default tenants
		tenants =Locataire.objects.order_by("-id")
		context = { 'tenants': tenants}
	return render(request,'loyer/tenant.html', context)

@login_required(login_url='is_locatire') 
def calendar(request):
	search_post = request.GET.get('search')
	if search_post:
		tenants =calender = Calender.objects.filter(Q(start_rent_date__icontains=search_post))
		context = { 'calender': calender}
	else:
	# If not searched, return default tenants
		tenants =calender = Calender.objects.order_by("-id")
		context = { 'calender': calender}
	return render(request,'loyer/calendar.html',context)


# --------------------------office------------------------------
@login_required 
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

@login_required 
def office_update(request, id, template_name='loyer/officeform.html'):
	post= get_object_or_404(Office, id=id)
	form = OfficeForm(request.POST, request.FILES, instance=post)
	if form.is_valid():
		form.save()
		return redirect('office')
	return render(request, template_name, {'form':form})
@login_required 
def office_detail(request, id, template_name = 'loyer/officedetail.html'):
	office = get_object_or_404(Office, id=id)
	return render(request, template_name, {'office':office})
@login_required 
def  office_destroy(request, id):  
	post = Office.objects.get(id=id)  
	post.delete()  
	return redirect("/office")  

@login_required 
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
@login_required 
def tenant_update(request, id, template_name='loyer/tenantform.html'):
	post= get_object_or_404(Locataire, id=id)
	form = LocataireForm(request.POST, request.FILES, instance=post)
	if form.is_valid():
		form.save()
		return redirect('/tenant')
	return render(request, template_name, {'form':form})


@login_required 
def  tenant_destroy(request, id):  
	post = Locataire.objects.get(id=id)  
	post.delete()  
	return redirect("/tenant")  


@login_required 
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

@login_required 
def calender_update(request, id, template_name='loyer/calendarform.html'):
	post= get_object_or_404(Calender, id=id)
	form = CalenderForm(request.POST, request.FILES, instance=post)
	if form.is_valid():
		form.save()
		return redirect('/calendar')
	return render(request, template_name, {'form':form})


@login_required 
def  calender_destroy(request, id):  
	post = Calender.objects.get(id=id)  
	post.delete()  
	return redirect("/calendar")  


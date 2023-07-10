from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from  .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import logout as auth_logout
from .import models
from main.models import Contact as contacts
from main.models import Offer as offers
from .forms import ImpressionForm, ImpressionForm1, AddCustomerForm
from .models import Customers
from django.db.models import Q

def handler404(request, exception):
    return render(request, 'dash/404.html', status=404)

def handler500(request):
    return render(request, 'dash/500.html', status=500)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Renamed to auth_login
            messages.success(request, 'If you were a hacker, congratulations. You are in!')
            return redirect('dash-home')
        else:
            messages.info(request, 'Helytelen felhasználónév vagy jelszó')
    else:
        return HttpResponse('Sztem próbáld újra néha szarakszik a rendszer')
    context = {}
    return render(request, 'dash/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

# Create your views here.
@login_required(login_url='login')
def home(request):
    learn = models.Learn.objects.all()
    contact = contacts.objects.all().order_by('-created')
    offer = offers.objects.all()
    impres = models.Impressions.objects.filter(status='pending')
    offer_count = offers.objects.all().count()
    income = Customers.calculate_total_income()
    cost = Customers.calculate_total_cost()
    websites_count = Customers.objects.all().count()
    
    context = {'learn': learn, 'contact': contact, 'offers': offer, 'impres': impres, 'offer_count': offer_count, 'income': income, 'websites_count': websites_count, 'cost': cost,}
    return render(request, 'dash/index.html', context)

@login_required(login_url='login')
def offerRequest(request, pk):
    offer = offers.objects.get(created=pk)
    
    context = {'offers': offer}
    return render(request, 'dash/offer.html', context)

@login_required(login_url='login')
def offerRequests(request):
    offer = offers.objects.all()
    
    context = {'offers': offer}
    return render(request, 'dash/offers.html', context)

@login_required(login_url='login')
def Contact(request, pk):
    contact = contacts.objects.get(id=pk)
    
    context = {'contacts': contact}
    return render(request, 'dash/message.html', context)

@login_required(login_url='login')
def Contacts(request):
    contact = contacts.objects.all()
    
    context = {'contact': contact}
    return render(request, 'dash/messages.html', context)

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Renamed to auth_login
            messages.success(request, 'If you were a hacker, congratulations. You are in!')
            return redirect('dash-home')
        else:
            messages.info(request, 'Helytelen felhasználónév vagy jelszó')
            
    context = {}
    return render(request, 'dash/login.html', context)

@login_required(login_url='login')
def logout_view(request):
    auth_logout(request)
    return redirect('login')


def SendImpression(request):
    form = ImpressionForm()
    
    if request.method == 'POST':
        form = ImpressionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Success!')
        else:
            messages.error(request, 'The submit was not succesful!')
            
    context = {'form': form}
    return render(request, 'dash/impression.html', context)

@login_required(login_url='login')
def ManageImpressions(request):
    
    context = {}
    return render(request, 'dash/manage-imp.html', context)

@login_required(login_url='login')
def ApprovedImpressions(request):
    impression = models.Impressions.objects.filter(status='approved')
    title = 'Approved Impressions'
    
    context = {'impression': impression, 'title': title}
    return render(request, 'dash/impression-arp.html', context)

@login_required(login_url='login')
def RejectedImpressions(request):
    impression = models.Impressions.objects.filter(status='rejected')
    title = 'Rejected Impressions'
    
    context = {'impression': impression, 'title': title}
    return render(request, 'dash/impression-arp.html', context)

@login_required(login_url='login')
def PendingImpressions(request):
    impression = models.Impressions.objects.filter(status='pending')    
    
    title = 'Pending Impressions'
    
    context = {'impression': impression, 'title': title}
    return render(request, 'dash/impression-arp.html', context)

@login_required(login_url='login')
def ChangeStatusImpression(request, pk, pk1):
    impression = models.Impressions.objects.get(id=pk, status=pk1)
    form = ImpressionForm1(instance=impression)
    
    if request.POST:
        form = ImpressionForm1(request.POST, instance=impression)
        if form.is_valid():
            form.save()
            messages.success(request, 'The object has been updated!')
            return redirect('manage')
        else:
            messages.info(request, 'Fail!')
     
    context = {'impression': impression, 'form': form}
    return render(request, 'dash/impression-sc.html', context)

@login_required(login_url='login')
def Customer(request):
    customers = Customers.objects.all()
    
    context = {'customers': customers}
    return render(request, 'dash/customers.html', context)

@login_required(login_url='login')
def CustomerDetails(request, pk, pk1):
    customer = Customers.objects.get(name=pk, user_id=pk1)
    
    context = {'customer': customer}
    return render(request, 'dash/customer.html', context)

@login_required(login_url='login')
def AddCustomer(request):
    form = AddCustomerForm()
    
    if request.POST:
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Uploaded!')
        else:
            messages.error(request, 'Fail!')
            
    context = {'form': form}
    return render(request, 'dash/add-customer.html', context)

@login_required(login_url='login')
def SearchCustomer(request):
    search = ''
    customers = Customers.objects.none()  # Initialize with an empty queryset
    
    if request.POST:
        search = request.POST.get('search-customer', '')
        customers = Customers.objects.filter(Q(name__contains=search) | Q(email__icontains=search) | Q(user_id__icontains=search) | Q(website__icontains=search) | Q(host_email__icontains=search))
    
    context = {'search': search, 'customers': customers}
    return render(request, 'dash/search-customer.html', context)

@login_required(login_url='login')
def Learn(request, pk):
    learn = models.Learn.objects.get(id=pk)
    
    context = {'learn': learn}
    return render(request, 'dash/learn.html', context)
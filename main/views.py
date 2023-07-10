from django.shortcuts import render, redirect
from .import forms
from django.contrib import messages
from dashboard.models import Impressions
# Create your views here.

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def home(request):
    impres5 = Impressions.objects.filter(star=5)[0:2]
    
    context = {'impres5': impres5}
    return render(request, 'index.html', context)

def aboutUs(request):
    return render(request, 'about.html')

def contactUs(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success!')
            return redirect('contact')
        else:
            messages.error(request, 'Something went wrong, try again later or please send me an email: web\'still@gmail.com')
    context = {'form': form}
    return render(request, 'contact.html', context)

def Impressionses(request):
    impres1 = Impressions.objects.filter(star=1, status='approved')
    impres2 = Impressions.objects.filter(star=2, status='approved')
    impres3 = Impressions.objects.filter(star=3, status='approved')
    impres4 = Impressions.objects.filter(star=4, status='approved')
    impres5 = Impressions.objects.filter(star=5, status='approved')
    
    context = {'impres1': impres1, 'impres2': impres2, 'impres3': impres3, 'impres4': impres4, 'impres5': impres5}
    return render(request, 'impressions.html', context)

def pricing(request):
    return render(request, 'pricing.html')

def reference(request):
    return render(request, 'reference.html')

def responsive(request):
    return render(request, 'responsive.html')

def services(request):
    return render(request, 'services.html')

def collega(request):
    return render(request, 'team-member.html')

def WebDev(request):
    return render(request, 'webdeveloping.html')

def Process(request):
    context = {}
    return render(request, 'work-process.html', context)

def success(request):
    return render(request, 'successfully.html')

def offerRequest(request):
    form = forms.Basic()
    
    if request.method == 'POST':
        form = forms.Basic(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The offer request was successful!')
            return redirect('success')
        else:
            messages.error(request, 'The offer request was not successful!')
    
    context = {'form': form}
    return render(request, 'offer-request.html', context)
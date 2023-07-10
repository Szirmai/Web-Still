from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'



urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.aboutUs, name='about'),
    path('contact-us/', views.contactUs, name='contact'),
    path('impressions/', views.Impressionses, name='ops'),
    path('pricing/', views.pricing, name="pricing"),
    path('references/', views.reference, name='reference'),
    path('responsiveness/', views.responsive, name='resp'),
    path('services/', views.services, name='services'),
    path('collega/', views.collega, name='collega'),
    path('blog/webdeveloping-nowadays/', views.WebDev, name='web-dev'),
    path('work-process/', views.Process, name='process'),
    path('offer-request/', views.offerRequest, name='offer-request'),
    path('successful-request/', views.success, name='success'),
]
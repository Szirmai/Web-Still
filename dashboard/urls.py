from django.urls import path
from .import views
from django.conf.urls import handler404, handler500

handler404 = 'dashboard.views.handler404'
handler500 = 'dashboard.views.handler500'


urlpatterns = [
    path('', views.home, name='dash-home'),
    path('offer-requests/<str:pk>', views.offerRequest, name='offer-reque'),
    path('contact-us/<str:pk>', views.Contact, name='contacts'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('offer-requests/', views.offerRequests, name='offer-requests'),
    path('contact-us/', views.Contacts, name='contact-us'),
    path('impression/send/code', views.SendImpression, name='send-impression'),
    path('impression/manage/', views.ManageImpressions, name='manage'),
    path('impression/rejected/', views.RejectedImpressions, name='impression-r'),
    path('impression/approved/', views.ApprovedImpressions, name='impression-a'),
    path('impression/pending/', views.PendingImpressions, name='impression-p'),
    path('impression/change-status/<int:pk>/<str:pk1>', views.ChangeStatusImpression, name='impression-sc'),
    path('customer/', views.Customer, name='customer'),
    path('customers/<str:pk>/<str:pk1>/', views.CustomerDetails, name='customer-details'),
    path('customers/add-customer/', views.AddCustomer, name='add-customer'),
    path('customer/search/', views.SearchCustomer, name='search-customer'),
    path('larn/<str:pk>/', views.Learn, name='learn'),
]

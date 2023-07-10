from django.db import models
import uuid
from django.db.models import Sum

# Create your models here.
STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

class Learn(models.Model):
    name = models.CharField(max_length=130)
    created = models.DateTimeField(auto_now_add=True, null=True)
    tutorials = models.TextField(max_length=10000)
    details = models.TextField(max_length=100000)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-created']
        
class Impressions(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    picture_choice = (
        (1, '✨'),
        (2, '✨✨'),
        (3, '✨✨✨'),
        (4, '✨✨✨✨'),
        (5, '✨✨✨✨✨')
    )
    star = models.PositiveIntegerField(choices=picture_choice)
    impression = models.TextField(max_length=1000000)
    accept = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-created']
        

class Customers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    host_pwd = models.CharField(max_length=200)
    host_email = models.EmailField(max_length=200)
    admin_username = models.CharField(max_length=200)
    admin_password = models.CharField(max_length=200)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    website = models.URLField()
    cost = models.IntegerField()
    income = models.IntegerField()
    created = models.DateField(auto_now_add=True, null=True)
    
    def calculate_total_income():
        total_income = Customers.objects.aggregate(total_income=Sum('income'))['total_income']
        return total_income or 0
    
    def calculate_total_cost():
        total_cost = Customers.objects.aggregate(total_cost=Sum('cost'))['total_cost']
        return total_cost or 0
    
    def __str__(self):
        return str(self.user_id)
    
    class Meta:
        ordering = ['-created']
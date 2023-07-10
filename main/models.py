from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Pack1(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Pack2(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Pack3(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Pack4(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Pack5(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Pack6(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Pack7(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Pack8(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Pack9(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

class Pack10(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

class Pack11(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

class Pack12(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class WebsiteType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Goal(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Offer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    pack1 = models.ForeignKey(Pack1, on_delete=models.CASCADE, null=True, blank=True, default=1)
    pack2 = models.ForeignKey(Pack2, on_delete=models.CASCADE, null=True, blank=True, default=1)
    pack3 = models.ForeignKey(Pack3, on_delete=models.CASCADE, null=True, blank=True, default=1)
    pack4 = models.ForeignKey(Pack4, on_delete=models.CASCADE, null=True, blank=True, default=2)
    pack6 = models.ForeignKey(Pack6, on_delete=models.CASCADE, null=True, blank=True, default=2)
    pack7 = models.ForeignKey(Pack7, on_delete=models.CASCADE, null=True, blank=True, default=2)
    pack8 = models.ForeignKey(Pack8, on_delete=models.CASCADE, null=True, blank=True, default=2)
    pack9 = models.ForeignKey(Pack9, on_delete=models.CASCADE, null=True, blank=True, default=2)
    pack10 = models.ForeignKey(Pack10, on_delete=models.CASCADE, null=True, blank=True, default=2)
    pack11 = models.ForeignKey(Pack11, on_delete=models.CASCADE, null=True, blank=True, default=2)
    pack12 = models.ForeignKey(Pack12, on_delete=models.CASCADE, null=True, blank=True, default=2)
    WebsiteType = models.ForeignKey(WebsiteType, on_delete=models.CASCADE, null=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True)
    aboutproject = models.TextField(max_length=10000, null=True, blank=True)
    extra = models.TextField(max_length=10000, null=True, blank=True)
    SpecialWish = models.TextField(max_length=10000, null=True, blank=True)
    accept = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        
        
class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=700000)
    accept = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
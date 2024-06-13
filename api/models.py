from django.db import models
from django import forms

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CustomerForm(forms.ModelForm):
    excel_file = forms.FileField()  # new file field
    
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'date_of_birth', 'excel_file']  # include new field in form
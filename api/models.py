from django.db import models
from django import forms

# Define the Customer model
class Customer(models.Model):
    # Define a CharField for the first_name attribute with a maximum length of 60
    first_name = models.CharField(max_length=60)
    # Define a CharField for the last_name attribute with a maximum length of 60
    last_name = models.CharField(max_length=60)
    # Define a DateField for the date_of_birth attribute
    date_of_birth = models.DateField()

    # Define the string representation of a Customer instance
    def __str__(self):
        # Return the first_name and last_name of the Customer instance
        return f'{self.first_name} {self.last_name}'

# Define the CustomerForm form
class CustomerForm(forms.ModelForm):
    # Define a FileField for the excel_file attribute
    excel_file = forms.FileField()  # new file field
    class Meta:
        # Specify the model associated with the form
        model = Customer
        # Specify the fields to include in the form
        fields = ['first_name', 'last_name', 'date_of_birth', 'excel_file']  # include new field in form
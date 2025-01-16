from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    # t = models.TextChoices()
    email = forms.EmailField()
from django.forms import ModelForm
from accounts.models import Customer
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Customer
        field = '__all__'
        exclude = ['user']
from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        models = Customer
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

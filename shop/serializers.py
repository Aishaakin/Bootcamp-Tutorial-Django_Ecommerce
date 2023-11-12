from .models import Product
from rest_framework import serializers
# Create your tests here.
class Slizer_4Shop(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = Product
         fields = ['name','price','cartegory1']
    


from rest_framework import serializers
from rest_framework.reverse import reverse


from .models import Template,Category,Product,Billing,Ratings




class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = '__all__'
class BillingSerializer(serializers.ModelSerializer):


    class Meta:
        model = Billing
        fields = '__all__'
class RatingsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Ratings
        fields = '__all__'
        
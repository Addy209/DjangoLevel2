from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'
    
class SpecsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Specifications
        fields='__all__'

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserReview
        fields='__all__'
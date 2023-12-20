from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
import bleach
from .models import MenuItem
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    #price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2) #data validation

    def validate_title(self, value):
        return bleach.clean(value)
    
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory', 'category', 'category_id']
        #data validation
        extra_kwargs = {
        'price': {'min_value': 2},
        'inventory':{'min_value': 0},
        'title': 
            {
                'validators': [
                    UniqueValidator(
                        queryset=MenuItem.objects.all()
                    )
                ]
            }
        }

        # #More ways for validating data
        # def validate_price(self, value):
        #     if (value < 2):
        #         raise serializers.ValidationError('Price should not be less than 2.0')
        
        # def validate_stock(self, value):
        #         if (value < 0):
        #             raise serializers.ValidationError('Stock cannot be negative')
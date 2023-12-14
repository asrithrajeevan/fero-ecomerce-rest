from django.utils import timezone
from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []},  # Disable default unique validation
        }

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []},  # Disable default unique validation
        }

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate_order_date(self, value):
        # Validate order date not in the past
        if value < timezone.now().date():
            raise serializers.ValidationError("Order date cannot be in the past.")
        return value

    def validate(self, data):
        # Validate cumulative weight of order items
        total_weight = sum(item['product'].weight * item['quantity'] for item in data['order_item'])
        if total_weight > 150:
            raise serializers.ValidationError("Cumulative weight of order items cannot exceed 150kg.")
        return data

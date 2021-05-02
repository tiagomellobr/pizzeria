from rest_framework import serializers
from order.models import Flavor, Size, Pizza, Customer, OrderStatus, Order


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        if instance.status.pk <= 2:
            instance.note = validated_data.get('note', instance.note)
            instance.customer = validated_data.get('customer', instance.customer)
            instance.pizza.set(validated_data.get('pizza', instance.pizza))
        # else:
        #     raise serializers.ValidationError('You can\'t change this order anymore, just the status.')

        instance.save()

        return instance

from .models import Order
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):

    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='PENDING')
    quanity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['id', 'size', 'order_status','quanity']

class OrderDetailSerializer(serializers.ModelSerializer):

    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='PENDING')
    quanity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ['id','size', 'order_status','quanity', 'created_at', 'updated_at']

class StatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default='PENDING')

    class Meta:
        model = Order
        fields = ['order_status']

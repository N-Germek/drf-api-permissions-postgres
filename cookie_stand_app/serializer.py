from rest_framework import serializers
from .models import Stand


class StandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'location', 'owner', 'min_customer_per_hour', 'max_customer_per_hour', 'avg_cookie_sales', 'created_at', 'updated_at')
        model = Stand

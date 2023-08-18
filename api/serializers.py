from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from drone.models import Drone, Medication, Shipping


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ('serial_number', 'model', 'weigth_limit',
                  'battery_capacity', 'state')


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ('name', 'weight', 'code', 'image')


class ShippingSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Chack if battery of drone not below 25 percent and medicine weigth not bigger than weigth limit
        """

        if data['drone'].state != Drone.Status.IDLE:
            raise serializers.ValidationError(
                {'drone_state': 'Selected drone is not available'})

        if data['drone'].battery_capacity < 25:
            raise serializers.ValidationError(
                {'drone_battery': 'Drone battery cannot be less than 25 percent'})

        medications = data['medications']

        total_weigth = 0
        for med in medications:
            total_weigth += med.weight

        if data['drone'].weigth_limit <= total_weigth:
            raise serializers.ValidationError(
                {'drone_weigth_limit': f'Medications total weigth cannot be more than {data["drone"].weigth_limit}'})

        return data

    class Meta:
        model = Shipping
        fields = '__all__'

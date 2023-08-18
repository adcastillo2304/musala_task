from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from drone.models import Drone, Medication, Shipping
from .serializers import DroneSerializer, MedicationSerializer, ShippingSerializer

# Create your views here.


class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    @action(detail=False, methods=['GET'])
    def available_drones(self, request, *args, **kwargs):
        drones = self.get_queryset().filter(state=Drone.Status.IDLE)
        serializer = self.get_serializer(drones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def battery(self, request, pk=None, *args, **kwargs):
        drone = self.get_object()
        return Response({'battery_capacity': drone.battery_capacity})

    @action(detail=True, methods=['GET'])
    def medications(self, request, pk=None, *args, **kwargs):
        drone = self.get_object()
        shipping = drone.shippings.first()
        if shipping:
            data = MedicationSerializer(shipping.medications, many=True).data
        else:
            data = {}
        return Response(data, status=status.HTTP_200_OK)


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

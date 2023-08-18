from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Medication(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator('[+/%*]', inverse_match=True)]
    )
    weight = models.FloatField()
    code = models.CharField(
        max_length=100,
        validators=[RegexValidator(
            '^[A-Z0-9_]*$', message='Only uppercase letters, numbers and underscore allowed')]
    )
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class Drone(models.Model):

    class DroneModel(models.TextChoices):
        LIGHTWEIGHT = 'Lightweight', 'Lightweight'
        MIDDLEWEIGHT = 'Middleweight', 'Middleweight'
        CRUISERWEIGHT = 'Cruiserweight', 'Cruiserweight'
        HEAVYWEIGHT = 'Heavyweight', 'Heavyweight'

    class Status(models.TextChoices):
        IDLE = 'Idle', 'Idle'
        LOADING = 'Loading', 'Loading'
        LOADED = 'Loaded', 'Loaded'
        DELIVERING = 'Delivering', 'Delivering'
        RETURNING = 'Returning', 'Returning'

    serial_number = models.CharField(max_length=100, validators=[
                                     RegexValidator('^[0-9]', message="Insert only numbers")],
                                     unique=True)
    model = models.CharField(choices=DroneModel.choices,
                             default=DroneModel.LIGHTWEIGHT,
                             max_length=13)
    weigth_limit = models.FloatField(help_text='Value in grams',
                                     validators=[MinValueValidator(1),
                                                 MaxValueValidator(500)])
    battery_capacity = models.IntegerField(validators=[MinValueValidator(0),
                                                       MaxValueValidator(100)])
    state = models.CharField(choices=Status.choices,
                             default=Status.IDLE, max_length=10)

    class Meta:
        indexes = [
            models.Index(fields=['serial_number'])
        ]

    def __str__(self):
        return f'Drone {self.serial_number} with {self.battery_capacity} battery'


class Shipping(models.Model):
    drone = models.ForeignKey(
        Drone, on_delete=models.CASCADE, related_name='shippings')
    medications = models.ManyToManyField(Medication, related_name='shippings')

    class Meta:
        ordering = ['drone']

    def __str__(self):
        return f'Shipping of drone {self.drone.serial_number} and medications {self.medications}'

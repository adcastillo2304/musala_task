# Generated by Django 4.2.3 on 2023-08-03 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0005_remove_drone_medication_shipping'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shipping',
            options={'ordering': ['drone']},
        ),
        migrations.AlterField(
            model_name='shipping',
            name='drone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shippings', to='drone.drone'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='medications',
            field=models.ManyToManyField(related_name='shippings', to='drone.medication'),
        ),
    ]
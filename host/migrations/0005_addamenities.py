# Generated by Django 4.0.1 on 2022-06-30 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0004_aboutproperty'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenities', models.CharField(max_length=1000)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.property')),
            ],
            options={
                'db_table': 'amenities',
            },
        ),
    ]

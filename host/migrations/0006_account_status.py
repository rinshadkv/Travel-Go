# Generated by Django 4.0.1 on 2022-07-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0005_addamenities'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

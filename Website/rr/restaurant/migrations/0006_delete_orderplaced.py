# Generated by Django 4.2.7 on 2023-11-20 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_orderplaced'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderPlaced',
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-30 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_order_ordermob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermob',
            name='mobi',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderMob',
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-23 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_braintree_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
    ]

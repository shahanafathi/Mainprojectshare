# Generated by Django 5.1 on 2024-09-21 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_companyorder_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
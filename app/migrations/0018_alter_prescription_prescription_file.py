# Generated by Django 5.1 on 2024-10-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_prescription_medicine_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='prescription_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 2.0.3 on 2018-03-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0013_auto_20180315_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='patient_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

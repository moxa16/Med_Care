# Generated by Django 2.0.3 on 2018-03-16 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0017_medicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='contact_no',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
    ]

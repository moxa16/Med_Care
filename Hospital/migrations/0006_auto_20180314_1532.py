# Generated by Django 2.0.3 on 2018-03-14 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0005_auto_20180314_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.Hospital'),
        ),
        migrations.AlterField(
            model_name='records',
            name='is_checked_out',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='records',
            name='type1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='records',
            name='type2',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='records',
            name='type3',
            field=models.CharField(max_length=10),
        ),
    ]

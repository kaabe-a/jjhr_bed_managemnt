# Generated by Django 3.1.7 on 2021-02-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjrh_bed', '0002_auto_20210219_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedmnagement',
            name='Time',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening'), ('Night', 'Night')], default='Morning', max_length=24),
        ),
    ]

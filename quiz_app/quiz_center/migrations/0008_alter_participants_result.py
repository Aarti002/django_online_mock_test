# Generated by Django 3.2.5 on 2021-08-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_center', '0007_competitiontype_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_center', '0012_alter_participants_person_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='person_image',
            field=models.ImageField(default='', upload_to='Images/'),
        ),
    ]
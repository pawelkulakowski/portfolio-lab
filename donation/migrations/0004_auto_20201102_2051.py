# Generated by Django 3.1.3 on 2020-11-02 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]

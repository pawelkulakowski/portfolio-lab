# Generated by Django 3.1.3 on 2020-11-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0004_auto_20201102_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insitution',
            name='type',
            field=models.IntegerField(choices=[(1, 'Fundacja'), (2, 'Organizacja pozarządowa'), (3, 'Zbiórka lokalna')], default=1),
        ),
    ]

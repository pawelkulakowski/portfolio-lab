# Generated by Django 3.1.3 on 2020-11-18 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donation', '0009_auto_20201118_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='address',
            field=models.CharField(max_length=256, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='categories',
            field=models.ManyToManyField(to='donation.Category', verbose_name='Kategorie'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='city',
            field=models.CharField(max_length=128, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.insitution', verbose_name='Instytucja'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Odebrano'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(max_length=128, verbose_name='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_comment',
            field=models.TextField(verbose_name='Komentarz'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_date',
            field=models.DateField(verbose_name='Data odbioru'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_time',
            field=models.TimeField(verbose_name='Godzina odbioru'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Liczba worków'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='zip_code',
            field=models.CharField(max_length=64, verbose_name='Kod pocztowy'),
        ),
    ]
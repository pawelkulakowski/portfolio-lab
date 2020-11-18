from django.db import models
from django.contrib.auth.models import User

TYPES = (
    (1, 'Fundacja'),
    (2, 'Organizacja pozarządowa'),
    (3, 'Zbiórka lokalna'),
)

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

class Insitution(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Instytucja'
        verbose_name_plural = 'Instytucje'

class Donation(models.Model):
    quantity = models.IntegerField(default=0, verbose_name='Liczba worków')
    categories = models.ManyToManyField(Category, verbose_name='Kategorie')
    institution = models.ForeignKey(Insitution, on_delete=models.CASCADE, verbose_name='Instytucja')
    address = models.CharField(max_length=256, verbose_name='Adres')
    phone_number = models.CharField(max_length=128, verbose_name='Numer telefonu')
    city = models.CharField(max_length=128, verbose_name='Miejscowość')
    zip_code = models.CharField(max_length=64, verbose_name='Kod pocztowy')
    pick_up_date = models.DateField(verbose_name='Data odbioru')
    pick_up_time = models.TimeField(verbose_name='Godzina odbioru')
    pick_up_comment = models.TextField(verbose_name='Komentarz')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='donations', verbose_name='Użytkownik') # domyślnie nullem?
    is_taken = models.BooleanField(default=False, null=True, blank=True, verbose_name='Odebrano')

    def __str__(self):
        return f'Dotacja dla {self.institution}: {self.quantity} x {self.categories.name}' #do poprawy

    class Meta:
        verbose_name = 'Dar'
        verbose_name_plural = 'Dary'

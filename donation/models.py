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
        verbose_name_plural = 'Categories'

class Insitution(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Insitution, on_delete=models.CASCADE)
    address = models.TextField() # do sprawdzenia !!
    phone_number = models.IntegerField()
    city = models.CharField(max_length=128)
    zip_code = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='donations') # domyślnie nullem?
    is_taken = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'Dotacja dla {self.institution}: {self.quantity} x {self.categories.name}' #do poprawy

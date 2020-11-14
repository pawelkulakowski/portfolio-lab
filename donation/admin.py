from django.contrib import admin
from donation.models import Category, Insitution, Donation
admin.site.register(Category)
admin.site.register(Insitution)
admin.site.register(Donation)
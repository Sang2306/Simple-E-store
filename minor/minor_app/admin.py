from django.contrib import admin

from .models import *


# define admin for model
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Customer)
admin.site.register(Segment)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Ship)
admin.site.register(Category)
admin.site.register(SubCategory)

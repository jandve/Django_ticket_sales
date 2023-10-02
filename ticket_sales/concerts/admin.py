from django.contrib import admin
from .models.user import User
from .models.band import Band
from .models.place import Place
from .models.product import Product

# Register your models here.
admin.site.register(User)
admin.site.register(Band)
admin.site.register(Place)
admin.site.register(Product)